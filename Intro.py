import pyxel
import time
from assets.character.main.haut2 import *
from assets.character.pnj.yakuchat import *
from assets.character.pnj.pawrain import *
class Intro():
    def __init__(self):
        self.cat_pos_x = 647
        self.cat_pos_y = 535
        self.up = True

    def go_up(self):
        self.cat_pos_y -= 5
        test.dess()

    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(1).load(0,0,"../assets/intro/"+ str(x) + str(y)+".png")
                pyxel.blt(x*225,y*170,1,0,0,225,170)
        Haut().dess(self.cat_pos_x,self.cat_pos_y,self.up)
        Yakuchat().dess(615,130)
        Yakuchat().dess(700,130)
        Pawrain().dess(700,250)


pyxel.init(1350,680)
test = Intro()
def update():
    if not test.cat_pos_y == 300:
        test.up = True
    else:
        test.up = False
        #La il faudra inserer la chatbox
        if pyxel.btnp(pyxel.KEY_SPACE): #La on met un autre booléen qui signifie la fin de la chatbox
            test.cat_pos_y -= 5
    if test.cat_pos_y <= 150:
        test.up = False
    #La le jeu peut démarrer


def draw():
    if test.up:
        test.go_up()
    test.dess()

pyxel.run(update,draw)