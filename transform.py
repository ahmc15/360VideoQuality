# using the same coordinate system as the 360 Libfrom: X points to the front of the sphere, Y is the top of the sphere, Z is the right side of the sphere.
# longitute is Phi, ranges from -pi to pi and stars from X and increases in counter-clockwise 
# latitude is Theta, ranges from -pi/2 to pi/2 and strart in the equator and increases upwards
# 
import numpy as np

def xyz_2_polar(x: float, y:float, z:float):
    phi= 

    return pass

def 2Dcoord_3Dcoord(m,n,H,W):
    u = (m+0.5)/W
    v = (n+0.5/H)
    Phi = (u-0.5)*(2*np.pi)
    Theta = (0.5-v)*np.pi
    
    return Theta, Phi


def EQP():
    pass
print("transforms")