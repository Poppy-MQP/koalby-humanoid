"""Primitive manager- receive events on a predetermined interval and log as commands. merge same-time commands into single cmd

methods:
init() - initializes primitive manager
add(primitive) - adds primitive to the queue
remove(primitive) - remove primitive to the queue
list() - lists all primitives currently in manager
update() - combines primitive commands into single commands and then sends to motors
stop() - stops the primitive manager
"""