import pyxel
from chatbox import Chatbox
from assets.character.main.haut2 import *
from assets.character.pnj.yakuchat import *
from assets.character.pnj.pawrain import *
from assets.character.pnj.pnjheads.orange_head import Orange_Head
from assets.character.pnj.pnjheads.pawrain_head import Pawrain_Head
from salles import Salle



class Intro():
    def __init__(self):
        self.cat_pos_x = 647
        self.cat_pos_y = 535
        self.up = True
        self.jouer = True
        
        self.Decor = Salle([], "Intro", [], [])
        self.pawrain_fin = Chatbox(Pawrain_Head(), self.Decor,{}, "Pawrain", "Si cette fois, tu ne reussis pas a rembourser tes dettes, je m'occuperai personnellement  de toi.")
        self.chatbox_pawrain_mission = Chatbox(Pawrain_Head(), self.Decor,{1: self.pawrain_fin}, "Pawrain", "Bon je te donne une derniere chance de te ratrapper, tu dois liquider le casino d'un de   mes ennemis.")
        self.chatbox_pawrain_retrouvailles = Chatbox(Pawrain_Head(), self.Decor, {1: self.chatbox_pawrain_mission}, "Pawrain", "Kot, tu te souviens de moi? Tu me dois beaucoup d'argent tu sais ?")

        self.Decor.current_chatbox = self.chatbox_pawrain_retrouvailles

    def go_up(self):
        self.cat_pos_y -= 5

    def dess(self):
        #dessinage de la salle
        for x in range(6):
            for y in range(4):
                pyxel.image(1).load(0,0,"assets/intro/"+ str(x) + str(y)+".png")
                pyxel.blt(x*225,y*170,1,0,0,225,170)
        #placement des differents persos de la scene
        Haut().dess(self.cat_pos_x,self.cat_pos_y,self.up)
        Yakuchat().dess(615,130)
        Yakuchat().dess(700,130)
        Pawrain().dess(700,250)



    def update(self):
        if not self.cat_pos_y == 300:
            self.up = True
        else:
            self.up = False

            #La il faudra inserer la chatbox
            if pyxel.btnp(pyxel.KEY_E) and not self.Decor.current_chatbox.chatbox_activated: #La on met un autre booléen qui signifie la fin de la chatbox
                self.cat_pos_y -= 5
        if self.cat_pos_y <= 150:
            
            self.up = False
            self.jouer = False
        #La le jeu peut démarrer

    def draw(self):
        if self.up:
            self.go_up()
        self.dess()
        if not self.up:
            self.Decor.current_chatbox.dess()
                    
