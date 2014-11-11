__author__ = 'Kheder'
import time as tm
import numpy as np
import bein
from my3Dplot import *

class robot(object):
    def __init__(self):
        self.stepTime = 0.5
        self.bein = bein.bein()
        self.mP = my3DFig(1)


    def genPosList(self):
        list = []
        for i in range(4):
            list.append(np.array([i,i+1,i+2]))
        return list

    def genDreieck(self,gn = 2,verschiebung = 0):
        l = []
        for i in range(gn):
            l.append(np.array([1,verschiebung,0])/(gn-i))
        for i in range(gn):
            l.append(np.array([-1,verschiebung,1])/gn+l[len(l)-1])
        for i in range(gn):
            l.append(np.array([-1,verschiebung,-1])/gn+l[len(l)-1])
        for i in range(gn):
            l.append(np.array([1,verschiebung,0])/gn+l[len(l)-1])

        return l


    def move(self):
        go = 0
        #liste = self.genPosList()
        liste = self.genDreieck()
        while go < len(liste):
            t1 = tm.time()
            #self.bein.setPos(liste[go])
            temp = self.bein.setPos(liste[go])
            self.mP.setAnzahl(2)
            self.mP.setLegPos(0, temp)
            self.mP.update()
            print(go)
            td = tm.time() - t1
            if td < self.stepTime:
                tm.sleep(self.stepTime-td)
            else:
                print("Zulange gebraucht")

            go+=1
