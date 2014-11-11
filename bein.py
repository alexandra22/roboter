__author__ = 'Kheder'
import numpy as np


class bein(object):
    def __init__(self):
        self.Os = np.array([0,0,0])
        self.Pos = self.Os

    def setPos(self, Pos):
        self.Pos = self.Os + Pos
        print(self.Pos)
        return self.Pos

