import pyxel
from random import randint
import time
class Des:
    def __init__(self):
        self.de1 = "1"
        self.de2 = "2"
        self.i = 6
        
        self.jouer = True
        self.range_x = [595, 705]
        self.range_y = [375, 405]


    def affichage(self, de1, de2):
        if not self.de1 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de1 + ".png")
            pyxel.blt(425,100,0,0,0,200,200)
        if not self.de2 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de2 + ".png")
            pyxel.blt(725, 100, 0, 0, 0, 200, 200)

    def tirer(self):
        i = 0


    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.jouer = False

    def draw(self):
        pyxel.cls(1)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.tirer()
        if self.i < 6:
            self.i+=1
            self.affichage(str(self.i),str(self.i))