import pyxel
from random import randint
from assets.font.PyxelUnicode import PyxelUnicode
import time
class Des:
    def __init__(self, CHAT):
        pyxel.mouse(False)
        self.CHAT = CHAT
        self.range_x = [595, 705]
        self.range_y = [375, 405]
        
        self.de1 = "1"
        self.de2 = "2"
        self.couleur_mise_1 = 9
        self.couleur_mise_2 = 9
        self.couleur_mise_3 = 9
        self.argent_joue = 0
        self.bets = []
        self.jouer = True
        self.font1 = PyxelUnicode("assets/font/pixelmix.ttf", 30)
        self.font2 = PyxelUnicode("assets/font/pixelmix.ttf", 50)
        #permet de faire l'animation des dés
        self.frame = 0
        self.i = 6
        self.j = 6
        self.k = 2



    def affichage_des_resultats(self, de1, de2):
        if not self.de1 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de1 + ".png")
            pyxel.blt(425,100,0,0,0,200,200)
        if not self.de2 is None:
            pyxel.image(0).load(0, 0, "assets/des/" + de2 + ".png")
            pyxel.blt(725, 100, 0, 0, 0, 200, 200)

    def affichage(self):
        #affichage de l'argent, de ce qu'on peut miser
        pyxel.rect(1000, 100, 50, 50, self.couleur_mise_1)
        pyxel.rect(1000, 200, 50, 50, self.couleur_mise_2)
        pyxel.rect(1000, 300, 50, 50, self.couleur_mise_3)
        self.font2.text(1060, 97, "1000 $w$")
        self.font2.text(1060, 197, "500 $w$")
        self.font2.text(1060, 297, "250 $w$")
        self.font2.text(50, 30, str(self.CHAT.money)+" $w$")

    def affichage_des_nombres(self):
        #affiche les nombres
        self.font1.text(160,500,"2")
        self.font1.text(240, 500, "3")
        self.font1.text(320, 500, "4")
        self.font1.text(400, 500, "5")
        self.font1.text(480, 500, "6")
        self.font1.text(560, 500, "7")
        self.font1.text(640, 500, "8")
        self.font1.text(720, 500, "9")
        self.font1.text(800, 500, "10")
        self.font1.text(890, 500, "11")
        self.font1.text(980, 500, "12")
        
        #affichage des nombres sélectionnés
        for n in self.bets:
            if n <11:
                self.font1.text(n * 80,500,str(n),color=10,bg_color=0)
            if n ==11:
                self.font1.text(890,500,"11",color=10,bg_color=0)
            if n ==12:
                self.font1.text(980,500,"12",color=10,bg_color=0)

    def tirer(self):
        self.i = 0
        self.j = 0
        self.k = 0
        self.de1 = str(randint(1,6))
        self.de2 = str(randint(1, 6))
        self.CHAT.money += self.money_won()
        #réinitialise le jeu
        self.argent_joue = 0
        self.couleur_mise_1 = self.couleur_mise_2 = self.couleur_mise_3 = 9
        while len(self.bets) != 0:
            self.bets.pop()

    def money_won(self):
        result = int(self.de1) + int(self.de2)
        #le joueur a parier sur une fourchette de 12
        if len(self.bets) == 2 and (self.bets[0] == 2 and self.bets[1] == 12):
            return self.argent_joue
        #le joueur a parié que sur un nombre
        if len(self.bets) == 1 and result == self.bets[0]:
            return self.argent_joue * 4
        if len(self.bets) == 1 and result != self.bets[0]:
            return 0
        #le joueur a parié sur une fourchette quelconque
        if (result in range(self.bets[0], self.bets[1] + 1)) or (result in range(self.bets[1], self.bets[0] + 1)):
            return self.argent_joue * round(2 - (len(self.bets) / 11))
        
        #le joueur a perdu
        return 0
             
        
    def chose_bets(self, number):
        if len(self.bets) == 2:
            self.bets.pop(0)
        self.bets.append(number)
    
    def chose_range_to_bet(self, x):
            if 160 <= x <= 185:
                self.chose_bets(2)
            if 240 <= x <= 265:
                self.chose_bets(3)
            if 320 <= x <= 345:
                self.chose_bets(4)
            if 400 <= x <= 425:
                self.chose_bets(5)
            if 480 <= x <= 505:
                self.chose_bets(6)
            if 560 <= x <= 585:
                self.chose_bets(7)
            if 640 <= x <= 665:
                self.chose_bets(8)
            if 720 <= x <= 745:
                self.chose_bets(9)
            if 800 <= x <= 825:
                self.chose_bets(10)
            if 890 <= x <= 915:
                self.chose_bets(11)
            if 980 <= x <= 1005:
                self.chose_bets(12)
        
    def select_wage(self, y):
        if 100<= y <= 150 and self.CHAT.money >= 1000 and self.couleur_mise_1 == 9:
            self.couleur_mise_1 = 10
            self.argent_joue += 1000
            self.CHAT.money -= 1000
        if 200<= y <= 250 and self.CHAT.money >= 500 and self.couleur_mise_2 == 9:
            self.couleur_mise_2 = 10
            self.argent_joue += 500
            self.CHAT.money -= 500
        if 300<= y <= 350 and self.CHAT.money >= 250 and self.couleur_mise_3 == 9:
            self.couleur_mise_3 = 10
            self.argent_joue += 250
            self.CHAT.money -= 250
        

    def update(self):
        #quitte le jeu
        if pyxel.btnp(pyxel.KEY_A):
            self.jouer = False
            pyxel.mouse(True)
            
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            #sélection de la mise 
            if 1000<=pyxel.mouse_x<=1050:
                self.select_wage(pyxel.mouse_y)
                    
            #choisis l'intervalle de pari       
            if 500<=pyxel.mouse_y<=540:
                self.chose_range_to_bet(pyxel.mouse_x)
                    
            
                    
        if pyxel.btnp(pyxel.KEY_O):
            print(str(self.argent_joue)+", "+str(self.CHAT.money))
            

    def draw(self):
        #lance les dés
        if pyxel.btnp(pyxel.KEY_SPACE) and len(self.bets) >= 1 and self.argent_joue > 0:
            self.tirer()
            
        #affichage des nombres, mises, argent, rrésultats et animation des dés
        if self.frame == 3:
            self.frame = 0
            pyxel.cls(1)
            self.affichage()
            self.affichage_des_nombres()
            if self.i < 6 and self.j > 1:
                self.i+=1
                self.j -=1
                self.affichage_des_resultats(str(self.i),str(self.j))
            elif self.k < 2:
                self.j = 6
                self.i = 1
                self.k += 1
                self.affichage_des_resultats(str(self.i), str(self.j))
                # if self.gagne():
                #     self.CHAT.money += 1.5 * self.argent_joue
            else:
                self.affichage_des_resultats(self.de1,self.de2)
        else:
            self.frame+=1
            
            
