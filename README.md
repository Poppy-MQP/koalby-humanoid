# koalby-humanoid

MQP Note: This kinematics branch last worked on 2/18/22. As of that time, the team determined that the way IK is 
        calculated in _goto doesn't function due to scipy.minimize bounds (dig down through the functions that 
        generate q). Would need to resolve this issue, or rewrite IK code from scratch to get things working. There 
        also seemed to be an issue with FK not using the top shoulder joint to calculate positions, but this was 
        tested less than the IK bug. 

We believe that the simplest path forward is likely to rewrite kinematics from scratch to make them more intuitive to use, however, if you wish to use this library, then solving the scipy.minimize issue is going to be the most important step.