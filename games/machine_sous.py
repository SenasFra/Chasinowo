import pyxel
import time
from random import randint

class Machine_a_Sous:
    def __init__(self):
        self.affiche = False
        self.assigned = ""
        self.x = 450
        self.y = 145
        self.final_a = 0
        self.final_b = -1
        self.final_c = 0
        self.jouer = True

    def launch(self):
        global a,b,c
        self.a = randint(1,100)
        self.b = randint(1,100)
        self.c = randint(1,100)

    def affichage(self):
        self.selection()
        self.machine()
        self.resultat()

    def machine(self):
        pyxel.rect(self.x + 50, self.y, 700, 400, 3)
        pyxel.rect(self.x, self.y + 50, 50, 300, 3)
        pyxel.rect(self.x + 750, self.y + 50, 50, 300, 3)
        pyxel.circ(self.x + 50, self.y + 50, 50, 3)
        pyxel.circ(self.x + 50, self.y + 349, 50, 3)
        pyxel.circ(self.x + 749, self.y + 50, 50, 3)
        pyxel.circ(self.x + 749, self.y + 349, 50, 3)
        pyxel.rect(self.x + 799, self.y + 299, 20, 10, 7)
        pyxel.rect(self.x + 819, self.y + 294, 20, 20, 7)
        pyxel.rect(self.x + 824, self.y + 144, 10, 150, 7)
        pyxel.circ(self.x + 829, self.y + 124, 20, 8)
        pyxel.rect(self.x + 300, self.y + 100, 200, 200, 1)
        pyxel.rect(self.x + 80, self.y + 100, 200, 200, 1)
        pyxel.rect(self.x + 520, self.y + 100, 200, 200, 1)

    def resultat(self):
        pyxel.rect(self.x+280,self.y-20,20,20,3)
        pyxel.rect(self.x+500,self.y-20,20,20,3)
        pyxel.rect(self.x+20,self.y-100,760,80,3)
        pyxel.circ(self.x+20,self.y-80,20,3)
        pyxel.circ(self.x+20,self.y-41,20,3)
        pyxel.rect(self.x,self.y-80,20,40,3)
        pyxel.circ(self.x+779,self.y-80,20,3)
        pyxel.circ(self.x+779,self.y-41,20,3)
        pyxel.rect(self.x+780,self.y-80,20,40,3)
        pyxel.rect(self.x + 20, self.y - 95, 760, 70, 7)
        if self.assigned == "abc" and self.final_a==self.final_b and self.final_b == self.final_c:
            pyxel.image(2).load(0,0,"assets/Machine_sous/oworo.png")
            pyxel.blt(self.x + 162, self.y - 90, 2, 0, 0, 36, 60)
            pyxel.blt(self.x + 382, self.y - 90, 2, 0, 0, 36, 60)
            pyxel.blt(self.x + 602, self.y - 90, 2, 0, 0, 36, 60)

    def assign(self,name):
        if "a" in name:
            if self.a <= 50:
                self.tire = "assets/Machine_sous/chat7.png"
                self.final_a = 1
            elif 50<self.a <= 75:
                self.final_a = 2
                self.tire = "assets/Machine_sous/chat_citron_casque.png"
            elif 75<self.a<= 95:
                self.tire = "assets/Machine_sous/chat_orange.png"
                self.final_a = 3
            else:
                self.tire = "assets/Machine_sous/chat_bar.png"
                self.final_a = 4
            pyxel.image(0).load(0, 0, self.tire)
            pyxel.blt(self.x+80, self.y+100, 0, 0, 0, 200, 200)
        if "b" in name:
            if self.b <= 50:
                self.tire = "assets/Machine_sous/chat7.png"
                self.final_b = 1
            elif 50<self.b <= 75:
                self.tire = "assets/Machine_sous/chat_citron_casque.png"
                self.final_b = 2
            elif 75<self.b <= 95:
                self.tire = "assets/Machine_sous/chat_orange.png"
                self.final_b = 3
            else:
                self.tire = "assets/Machine_sous/chat_bar.png"
                self.final_b = 4
            pyxel.image(0).load(0, 0, self.tire)
            pyxel.blt(self.x+300, self.y+100, 0, 0, 0, 200, 200)
        if "c" in name:
            if self.c <= 50:
                self.tire = "assets/Machine_sous/chat7.png"
                self.final_c = 1
            elif 50<self.c <= 75:
                self.tire = "assets/Machine_sous/chat_citron_casque.png"
                self.final_c = 2
            elif 75<self.c<= 95:
                self.tire = "assets/Machine_sous/chat_orange.png"
                self.final_c = 3
            else:
                self.tire = "assets/Machine_sous/chat_bar.png"
                self.final_c = 4
            pyxel.image(0).load(0, 0, self.tire)
            pyxel.blt(self.x+520, self.y+100, 0, 0, 0, 200, 200)

    def selection(self):
        pyxel.rect(self.x+180,self.y+450,440,101,3)
        pyxel.rect(self.x+160,self.y+470, 20,60,3)
        pyxel.rect(self.x + 620, self.y + 470, 20, 60, 3)
        pyxel.tri(self.x +180,self.y+450,self.x+160,self.y+470,self.x+180,self.y+470,3)
        pyxel.tri(self.x + 160, self.y + 530, self.x + 180, self.y + 530, self.x + 180, self.y + 550, 3)
        pyxel.tri(self.x + 639, self.y + 470, self.x + 619, self.y + 470, self.x + 619, self.y + 450, 3)
        pyxel.tri(self.x + 639, self.y + 530, self.x + 619, self.y + 530, self.x + 619, self.y + 550, 3)
    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.jouer = False

    def draw(self):
        pyxel.cls(1)
        self.affichage()
        self.assign(self.assigned)
        if "b" in self.assigned and not "c" in self.assigned:
            time.sleep(1)
            self.assigned += "c"
            self.assign(self.assigned)
        if "a" in self.assigned and not "b" in self.assigned:
            time.sleep(1)
            self.assigned += "b"
            self.assign(self.assigned)
        if not "a" in self.assigned and self.affiche:
            self.affichage()
            time.sleep(1)
            self.assigned = "a"
            self.assign(self.assigned)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and pyxel.pget(pyxel.mouse_x,pyxel.mouse_y) == 8:
            self.launch()
            self.affichage()
            self.assigned = ""
            self.affiche = True
