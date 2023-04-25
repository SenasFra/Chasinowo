import pyxel
import pickle
import time
import os

class Menu:
    def __init__(self):
        self.new = True
        self.continu = False
        self.exit = False
        self.charger = False
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
        if pyxel.btn(pyxel.KEY_E) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.new:
                self.jouer = False
            if self.continu:
                #vérification que la sauvegarde est valable
                with open('save/data.pickle', 'rb') as f:
                    if pickle.load(f)[0] >= 100:
                        self.charger = True
                        self.jouer = False
            if self.exit:
                pyxel.quit()
                

    def draw(self):
        if 500 < pyxel.mouse_x < 800 and 340 < pyxel.mouse_y < 380:
            
            self.new = True
            self.continu = False
            self.exit = False
            
        if 500 < pyxel.mouse_x < 800 and 390 < pyxel.mouse_y < 420:
            self.new = False
            self.continu = True
            self.exit = False
            
        if 500 < pyxel.mouse_x < 800 and 422 < pyxel.mouse_y < 455:
            self.new = False
            self.continu = False
            self.exit = True
            
            
        pyxel.cls(0)
        for x in range(6):
            for y in range(5):
                pyxel.image(0).load(0, 0, "assets/chatsbackground.png")
                pyxel.blt(x* 240, y * 150, 0, 0, 0, 232, 196)
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