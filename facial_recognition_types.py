## typedef (called class in python (I guess))
#(Waiting for Image Processing team)
#EyeL: X,Y
#EyeR: X,Y
#Mouth: X,Y
#Anything else I can use?

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)
    #str(p) -> '(3,4)'
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
##List