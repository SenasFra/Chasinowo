import pyxel
import salles
from machine_sous import Machine_a_Sous

class Debut:
    def __init__(self):
        self.mur = [[245,180,1070,700]]
        self.porte_bas = [625, 655, 700]
        self.porte_haut = [650, 680, 180]
        self.jeu = []

    def changer_haut(self):
        return salles.Deux()
    
    def changer_bas(self):
        return salles.Fin()


    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/debut/"+str(x)+str(y)+".png")
                pyxel.blt(x*232,y*196,0,0,0,300,300)


class Fin:
    def __init__(self):
        self.mur = [[170, 105, 1165, 720]]
        self.porte_bas = [] #650, 700, 720
        self.porte_haut = [630, 675, 105]
        self.jeu = []


    def changer_haut(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/fin/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 232, y * 196, 0, 0, 0, 300, 300)

class Deux:
    def __init__(self):
        self.mur = [[330, 205, 920, 640],[445, 260, 765, 460],[490,410,720,510],[490,210,720,310], [280,225,375,460],[330,240,435,360]]
        self.porte_bas = [620,675,640]
        self.porte_haut = []
        self.jeu = [380, 390]

    def jouer(self):
        return Machine_a_Sous()

    def changer_bas(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/2/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 232, y * 196, 0, 0, 0, 232, 196)
        for k in range(10):
            pyxel.rectb(self.jeu[0]+k,self.jeu[1]+k,75-2*k,75-2*k,8)