import pyxel
import time
import os

class Menu:
    def __init__(self):
        self.new = True
        self.continu = False
        self.exit = False
        self.jouer = True
    def update(self):
        if self.continu and pyxel.btnp(pyxel.KEY_S):
            self.continu = False
            self.exit = True
        if self.new and pyxel.btnp(pyxel.KEY_S):
            self.new = False
            self.continu = True
        if self.continu and pyxel.btnp(pyxel.KEY_Z):
            self.continu = False
            self.new = True
        if self.exit and pyxel.btnp(pyxel.KEY_Z):
            self.exit = False
            self.continu = True
        if pyxel.btn(pyxel.KEY_E):
            if self.new == True:
                self.jouer = False

    def draw(self):
        pyxel.cls(0)
        for xi in range(6):
            for yi in range(5):
                pyxel.image(0).load(0, 0, "assets/chatsbackground.png")
                pyxel.blt(xi* 240, yi * 150, 0, 0, 0, 232, 196)
        for x in range(2):
            for y in range(2):
                pyxel.image(1).load(0,0,"assets/menu/"+str(x)+str(y)+".png")
                pyxel.blt(425+x*250,210+y*130,1,0,0,250,130)
        if not self.new:
            pyxel.rect(425, 352, 110,20,0)
        if not self.continu:
            pyxel.rect(425, 390, 110,20,0)
        if not self.exit:
            pyxel.rect(425, 426, 110,20,0)