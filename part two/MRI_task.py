import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.animation as animation
import math

flag = True
flag2 = True
rotating_axis = [0,0,1]

def data_gen(num):
    global flag,flag2
    if flag2 is True:
        rotating_ang = num*np.pi/180
        if flag is True :    
            T1 = 200
            time = num
            M = (1-np.exp(-time/T1))
            pulse_ang = math.asin(M)
            print(pulse_ang)
        else:
            pulse_ang = 510*np.pi/(6*180)
    else:
        
        rotating_ang = 0
        pulse_ang = (85-(num-1440))*np.pi/180
    vector = [[3*np.cos(pulse_ang)*np.cos(rotating_ang)],[3*np.cos(pulse_ang)*np.sin(rotating_ang)],[3*np.sin(pulse_ang)]] 
    vx, vy, vz = vector
    ax.cla()
    ax.quiver(0, 0, 0, vx, vy, vz, pivot="tail", color="black", arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, vx, vy, 0, pivot="tail", color="black",
            linestyle="dashed", arrow_length_ratio=0.1)
    if num == 1114:
        flag = False
    if num == 1439:
        flag2 = False
    p1 = []
    p2 = []
    p3 = []
    for i in range(0, 1114, 4):
        M_ = (1-np.exp(-i/200))
        pulse_ang2 = math.asin(M_)
        rotating_ang2 = i*np.pi/180
        p3.append(3*np.sin(pulse_ang2))
        p2.append(3*np.cos(pulse_ang2)*np.sin(rotating_ang2))
        p1.append(3*np.cos(pulse_ang2)*np.cos(rotating_ang2))

    #ax.scatter(p1, p2, p3, c='b')
    ax.plot(p1, p2, p3, c='b')
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    ax.set_zlim(0,5)
    ax.view_init(elev=20., azim=32)
    x, y, z = np.zeros((3,3))
    u, v, w = np.array([[5,0,0],[0,5,0],[0,0,5]])
    ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1)
    ax.view_init(elev=35, azim=190)
    if num == 0:
        flag = True
        flag2 = True
    
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

data_gen(0)
ani = animation.FuncAnimation(fig, data_gen, range(1525), repeat = True, interval = 10)
plt.show()