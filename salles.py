import pyxel
import salles

class Debut:
    def __init__(self):
        self.mur = [245,179,1069,702]
        self.porte_bas = [627, 655, 702]
        self.porte_haut = [649, 682, 179]

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
        self.mur = [170, 103, 1165, 719]
        self.porte_bas = [] #650, 698, 719
        self.porte_haut = [632, 674, 103]


    def changer_haut(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/fin/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 232, y * 196, 0, 0, 0, 300, 300)

class Deux:
    def __init__(self):
        self.mur = [329, 205, 920, 639]
        self.porte_bas = [621,675,639]
        self.porte_haut = []


    def changer_bas(self):
        return salles.Debut()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, "assets/2/" + str(x) + str(y) + ".png")
                pyxel.blt(x * 232, y * 196, 0, 0, 0, 232, 196)