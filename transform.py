# using the same coordinate system as the 360 Libfrom: X points to the front of the sphere, Y is the top of the sphere, Z is the right side of the sphere.
# longitute is Phi, ranges from -pi to pi and stars from X and increases in counter-clockwise 
# latitude is Theta, ranges from -pi/2 to pi/2 and strart in the equator and increases upwards
# 
import numpy as np



def 2Dcoord_3Dcoord(m: float,n: float,H: float,W: float):
    '''
    transforma a coordenada 2D da projeção equiretangular em 
    Input:
        m = index of the colummns
        n = index of the rows
        H = size of the height
        W = size of the width        
    '''
    u = (m+0.5)/W
    v = (n+0.5/H)
    Phi = (u-0.5)*(2*np.pi)
    Theta = (0.5-v)*np.pi
    X = np.cos(Theta)*np.cos(Phi)
    Y = np.sin(Theta)
    Z = (-1)*np.cos(Theta)*np.sin(Phi)
    
    return X,Y,Z

def 2Dcoord_Polar(M: float,n: float,H: float,W: float):
    '''
    '''
    u = (m+0.5)/W
    v = (n+0.5/H)
    Phi = (u-0.5)*(2*np.pi)
    Theta = (0.5-v)*np.pi

    return Theta,Phi
    

def CMP_3Dcoord(m: float,n: float,f: int,H: float,W: float):
    
    Ah = H / 2  # face is a square. u
    Aw = W / 3  # face is a square. v
    u = (m + 0.5) * 2 / Ah - 1
    v = (n + 0.5) * 2 / Aw - 1
    if f == 0:
        x = 1.0
        y = -v
        z = -u 
    elif f == 1:
        x = -1.0
        y = -v
        z = u
    elif f == 2:
        x = u
        y = 1.0
        z = v
    elif f == 3:
        x = u
        y = -1.0
        z = -v
    elif f == 4:
        x = u
        y = -v
        z = 1.0
    elif f == 5:                                
        x = -u
        y = -v
        z = -1.0
            
    
    return x,y,z
print("transforms")