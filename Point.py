import numpy as np

#Coordinates
class Point:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
         
    #str(p), print(p) -> '(x=1, y=2, w=3, h=4)'
    def __str__(self):
        return '(x={0}, y={1}, w={2}, h={3})'.format(self.x, self.y, self.w, self.h)
    
    #necessary? pA+pB
    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.w + other.w, self.h + other.h
    
    #necessary? pA-pB
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.w - other.w, self.h - other.h
    
    def __truediv__(self, other):
        #pA > pB
        pA = Point(self.x if self.x > other.x else other.x,
                   self.y if self.y > other.y else other.y,
                   self.w if self.w > other.w else other.w,
                   self.h if self.h > other.h else other.h)
        pB = Point(self.x if pA.x == other.x else other.x,
                   self.y if pA.y == other.y else other.y,
                   self.w if pA.w == other.w else other.w,
                   self.h if pA.h == other.h else other.h)
       
        #div/0 error prevention. Returns self for later pDiff calculation.
        if pB.x == 0 or pB.y == 0 or pB.w == 0 or pB.h == 0:
            return self
        else:
            return pA.x / pB.x, pA.y / pB.y, pA.w / pB.w, pA.h / pB.h

#Screen resolution
#TODO: getter setter?
#TODO: Will the range of the values be different if the screen size if different?
##ImgProcess team might take care.
pScreenX = 1280
pScreenY = 720

#returns difference% in Point type.
def pDiff(p1, p2):
    pD = np.multiply(100, (p1 - p2))
    return Point(pD[0]/pScreenX, pD[1]/pScreenY, pD[2]/pScreenX, pD[3]/pScreenY)