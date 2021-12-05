"""Primitive manager- receive events on a predetermined interval and log as commands. merge same-time commands into single cmd

methods:
init() - initializes primitive manager
add(primitive) - adds primitive to the queue
remove(primitive) - remove primitive to the queue
primitives() - lists all primitives currently in manager
update() - combines primitive commands into single commands and then sends to motors
stop() - stops the primitive manager

currently uses pypot primitive class.
need to either rework and implement said class, or create new structure.
"""
import logging
import numpy

from collections import defaultdict
from functools import partial
from threading import Lock

# from ..utils.stoppablethread import StoppableLoopThread


logger = logging.getLogger(__name__)


class PrimitiveManager():  # originally uses param: StoppableLoopThread

    def __init__(self):

        # start a stobbableLoopThread

        self._prim = []
        # self._motors = motors
        self._filter = filter  # look into built in filter function to understand better

        self.syncing = Lock()

    def add(self, p):
        """ Add a primitive to the manager. The primitive automatically attached itself when started. """
        self._prim.append(p)

    def remove(self, p):
        """ Remove a primitive from the manager. The primitive automatically remove itself when stopped. """
        self._prim.remove(p)

    @property
    def primitives(self):
        """ List of all attached :class:`~pypot.primitive.primitive.Primitive`. """
        return self._prim

    def update(self):
        """ Combined at a predefined frequency the request orders and affect them to the real motors. """
        # may need to rework how this method functions, currently directly copied from pypot library
        with self.syncing:
            for m in self._motors:  # _motors can be recreated as a motor grouping system in KoalbyHumanoid.robot
                to_set = defaultdict(list)

                for p in self._prim:
                    for key, val in getattr(p.robot, m.name)._to_set.items():
                        to_set[key].append(val)

                for key, val in to_set.items():
                    if key == 'led':
                        colors = set(val)
                        if len(colors) > 1:
                            colors -= {'off'}
                        filtred_val = colors.pop()
                    else:
                        filtred_val = self._filter(val)

                    logger.debug('Combined %s.%s from %s to %s',
                                    m.name, key, val, filtred_val)
                    setattr(m, key, filtred_val)

            [p._synced.set() for p in self._prim]

    def stop(self):
        """ Stop the primitive manager. """
        for p in self.primitives[:]:
            p.stop()

        # StoppableLoopThread.stop(self)
