import numpy as np

def Centroid(shape, r):
    if shape.lower == 'circle':
        return  4*r/(3*np.pi)
    elif shape.lower == 'Ibeam':
        return 

def CentroidIBeam(b1, b2, h, t1, t2, t3):
    """  *****************
       \n* |- b1 -|      *
       \n*  ______  __   *
       \n* |__  __| __ t1*
       \n*    ||         *
       \n*t3->||<    h   *
       \n*  __||__  __   *
       \n* |______| __ t2*
       \n* |- b2- |      *
       \n*****************
        \nReturns the centroid from the bottom of the beam"""
    A1 = b1*t1
    y1 = t2+h+t1/2
    A2 = h*t3
    y2 = t2+h/2
    A3 = b2*t2
    y3 = t2/2
    y = (A1*y1+A2*y2+A3*y3)/(A1+A2+A3)
    return y

def MomentOfArea1Round(d, r=None):
    """ Also known as 'Q' or first moment of area
        d = diameter
        r = radius to point of interest"""
    A1 = np.pi/8*d**2
    y1 = Centroid('circle', d/2)
    if r != None:
        A2 = np.pi/4*(d/2-r)**2
        y2 = Centroid('circle', (d/2-r))+r
        return A1*y1+A2*y2
    return A1*y1

def MomentOfArea1IBeam(b1, b2, h, t1, t2, t3, point=1, custPoint=None):
    """ Calculates Q for the given geometry
        |- b1 -|
         ______  __
   2.   |__  __| __ t1
           ||
   1.  t3->||<    h
   3.    __||__  __
        |______| __ t2
        |- b2- |

        point -> integer 1-3 designating the point of interest,
        nuetral axis of beam (#1) is default
        
        custPoint overrides point and computes Q for the custom point"""
    ybar = CentroidIBeam(b1, b2, h, t1, t2, t3)
    if custPoint == None:
        if point == 1:
            A1 = b1*t1
            y1 = h+t2-ybar+t1/2
            A2 = (h+t2-ybar)*t3
            y2 = (h+t2-ybar)/2
            return A1*y1+A2*y2
        elif point == 2:
            A1 = t1*b1
            y1 = h+t2-ybar+t1/2
            return A1*y1
    