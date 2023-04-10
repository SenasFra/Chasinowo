import pyxel
import salles
from machine_sous import Machine_a_Sous
from des import Des

class Debut:
    def __init__(self):
        self.mur = [[270,140,1025,500]]
        self.porte_bas = [600, 690, 500]
        self.porte_haut = [595, 675, 140]
        self.porte_droit = []
        self.porte_gauche = [270, 240, 330]
        self.jeu = []

    def changer_haut(self):
        return salles.Deux()
    
    def changer_bas(self):
        return salles.Fin()

    def changer_gauche(self):
        return salles.Un()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/debut/"+str(x)+str(y)+".png")
                pyxel.blt(x*225,y*170,0,0,0,300,300)


class Fin:
    def __init__(self):
        self.mur = [[270, 145, 1025, 480], [395, 235, 590, 410], [340, 250, 645, 375], [460, 320, 540, 430], [445, 170, 540, 330], [860, 95, 1075, 215], [895, 175, 1055, 325], [840, 175,940,295]]
        self.porte_bas = []
        self.porte_haut = [590, 680, 145]
        self.porte_droit = []
        self.porte_gauche = []
        self.jeu = []


    def changer_haut(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/fin/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 225, y * 170, 0, 0, 0, 300, 300)

class Un:
    def __init__(self):
        self.mur = [[445, 165, 840, 450], [570, 220, 730, 380],[610, 200, 695, 395]]
        self.porte_bas = []
        self.porte_haut = []
        self.porte_droit = [840,340,430]
        self.porte_gauche = []
        self.jeu = []

    def changer_droit(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/1/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 225, y * 170, 0, 0, 0, 232, 196)

class Deux:
    def __init__(self):
        self.mur = [[385, 191, 925, 470],[330, 202, 436, 436],[543, 225, 760, 430], [494, 201, 588, 436],[720, 201, 812, 437], [880, 140, 975, 231]]
        self.porte_bas = [605,695, 470]
        self.porte_haut = []
        self.porte_gauche = []
        self.porte_droit = []
        self.jeu = [440, 375]

    def jouer(self):
        return Machine_a_Sous()

    def changer_bas(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/2/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 225, y * 170, 0, 0, 0, 232, 196)
        pyxel.image(0).load(0,0,"assets/character/greycat_.png")
        pyxel.blt(925,191,0,0,0,50,50)