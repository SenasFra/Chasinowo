import pyxel
from random import randint
import time
class Des:
    def __init__(self, CHAT):
        self.de1 = "1"
        self.de2 = "2"
        self.col1 = 9
        self.col2 = 9
        self.col3 = 9
        self.argent_joue = 0
        self.CHAT = CHAT
        self.parie = 2
        self.i = 6
        self.j = 6
        self.k = 2
        self.jouer = True
        self.frame = 0
        
        self.range_x = [595, 705]
        self.range_y = [375, 405]


    def affichageres(self, de1, de2):
        if not self.de1 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de1 + ".png")
            pyxel.blt(425,100,0,0,0,200,200)
        if not self.de2 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de2 + ".png")
            pyxel.blt(725, 100, 0, 0, 0, 200, 200)

    def affichage(self):
        pyxel.rect(1000, 100, 50, 50, self.col1)
        pyxel.rect(1000, 200, 50, 50, self.col2)
        pyxel.rect(1000, 300, 50, 50, self.col3)
        pyxel.image(2).load(0,0,"assets/chiffres/1.png")
        pyxel.blt(1070,110,2,0,0,20,35)
        pyxel.image(2).load(0, 0, "assets/chiffres/0.png")
        pyxel.blt(1105, 110, 2, 0, 0, 20, 35)
        pyxel.blt(1140, 110, 2, 0, 0, 20, 35)
        pyxel.blt(1175, 110, 2, 0, 0, 20, 35)
        pyxel.blt(1105, 210, 2, 0, 0, 20, 35)
        pyxel.blt(1140, 210, 2, 0, 0, 20, 35)
        pyxel.blt(1140, 310, 2, 0, 0, 20, 35)
        pyxel.image(2).load(0, 0, "assets/chiffres/5.png")
        pyxel.blt(1070, 210, 2, 0, 0, 20, 35)
        pyxel.blt(1105, 310, 2, 0, 0, 20, 35)
        pyxel.image(2).load(0, 0, "assets/chiffres/2.png")
        pyxel.blt(1070, 310, 2, 0, 0, 20, 35)
        pyxel.image(2).load(0,0,"assets/des/owo.png")
        pyxel.blt(1210,110,2,0,0,19,50)
        pyxel.tri(pyxel.mouse_x, pyxel.mouse_y, pyxel.mouse_x + 5, pyxel.mouse_y+10, pyxel.mouse_x-5, pyxel.mouse_y + 10, 7)

    def parier(self):
        if len(str(self.parie)) == 1:
            pyxel.image(0).load(0,0,"assets/chiffres/"+str(self.parie)+".png")
            pyxel.blt(675,350,0,0,0,20,35)
        else:
            pyxel.image(0).load(0, 0, "assets/chiffres/" + str(self.parie)[0] + ".png")
            pyxel.blt(655, 350, 0, 0, 0, 20, 35)
            pyxel.image(0).load(0, 0, "assets/chiffres/" + str(self.parie)[1] + ".png")
            pyxel.blt(675, 350, 0, 0, 0, 20, 35)

    def tirer(self):
        self.i = 0
        self.j = 0
        self.k = 0
        self.de1 = str(randint(1,6))
        self.de2 = str(randint(1, 6))
        if self.gagne():
            self.CHAT.money += 1.5 * self.argent_joue
        self.argent_joue = 0
        self.col1 = self.col2 = self.col3 = 9

    def gagne(self):
        return self.parie == int(self.de1) + int(self.de2)

    def update(self):
        pyxel.mouse(False)
        if pyxel.btnp(pyxel.KEY_A):
            self.jouer = False
            pyxel.mouse(True)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.pget(pyxel.mouse_x,pyxel.mouse_y) == 9:
                if 1000<=pyxel.mouse_x<=1050:
                    if 100<=pyxel.mouse_y<=150 and self.CHAT.money>=1000:
                        self.col1 = 10
                        self.argent_joue += 1000
                        self.CHAT.money -= 1000
                    if 200<=pyxel.mouse_y<=250 and self.CHAT.money>=500:
                        self.col2 = 10
                        self.argent_joue += 500
                        self.CHAT.money -= 500
                    if 300<=pyxel.mouse_y<=350 and self.CHAT.money>=250:
                        self.col3 = 10
                        self.argent_joue += 250
                        self.CHAT.money -= 250
        if pyxel.btnp(pyxel.KEY_Z) and self.parie<12:
            self.parie+=1
        if pyxel.btnp(pyxel.KEY_S) and self.parie>2:
            self.parie-=1
        if pyxel.btnp(pyxel.KEY_O):
            print(str(self.argent_joue)+", "+str(self.CHAT.money))

    def draw(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.tirer()
        if self.frame == 3:
            self.frame = 0
            pyxel.cls(1)
            self.affichage()
            self.parier()
            if self.i < 6 and self.j > 1:
                self.i+=1
                self.j -=1
                self.affichageres(str(self.i),str(self.j))
            elif self.k < 2:
                self.j = 6
                self.i = 1
                self.k += 1
                self.affichageres(str(self.i), str(self.j))
            else:
                self.affichageres(self.de1,self.de2)
        else:
            self.frame+=1
