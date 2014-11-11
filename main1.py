__author__ = 'Kheder'
import roboter
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, PathPatch
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import time
import numpy as np

def initCircle(self, mlist):
        """
        Funktion sur berechnung und Positionierung der Kreise in dem 3D-Plot
        :param mlist: ?????
        """
        if len(mlist) != self.__anzahl:
            print("initCircle:Error: Länge stimmt nicht überein!")
        else:
            for i in mlist:
                circle = Circle((i[0, 0], i[1, 0]), 1, color="b", alpha=0.5)
                self.__ax.add_patch(circle)
                art3d.pathpatch_2d_to_3d(circle, z=i[2, 0])
            plt.draw()

def main1():
    anzahl = 1
    __fig = plt.figure()
    __ax = __fig.gca(projection='3d')
    __xyz = [np.zeros(anzahl).tolist() for i in range(3)]
    __color = ['k'] * anzahl
    plt.ion()
    __ax.view_init(elev=40., azim=45)

        # Erstellt
    __newPoints = __ax.scatter(__xyz[0], __xyz[1], __xyz[2], c=__color)

    # Läst die Kreise erstellen wenn ihre Positionen verfügbar sind

    zeroPos = 1

    #if zeroPos is not None:
    #     initCircle(zeroPos)
    #     for i in range(len(zeroPos)):
    #         setLegPos(i, zeroPos[i])
    #    # Zeigt das Plotfester an
    __fig.show()
    time.sleep(2)
    print(__xyz[0][0])
    __newPoints = __ax.scatter(__xyz[0][0] + 1.0, __xyz[1], __xyz[2], c=__color)
    plt.draw()
    time.sleep(2)


if __name__ =="__main__":
    main1()

