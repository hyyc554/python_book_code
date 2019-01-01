from math import hypot


class Vextor(object):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)
