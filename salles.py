import pyxel
from games.machine_sous import Machine_a_Sous
from games.des import Des
from games.roulette import Roulette
from porte import Porte
from chatbox import Chatbox
from assets.character.pnj.greycat import Greycat
from assets.character.pnj.greycat_backward import Greycat_backward


class Salle:
    def __init__(self, coord_mur, img_name, jeux):
        self.hitbox = coord_mur
        self.portes = []
        self.img_name = img_name
        self.jeux = jeux
        self.cats = []
        self.chatboxes = []
        self.current_chatbox = None
        
    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, f"assets/{self.img_name}/{x}{y}.png")
                pyxel.blt(x*225, y*170, 0 ,0, 0, 225, 170)
        
        #affiche les chats        
        if len(self.cats) != 0:
            for cat in self.cats:
                cat["cat"].dess(cat["coord"][0], cat["coord"][1])
                
        #chatbox
        if self.current_chatbox is not None and self.current_chatbox.chatbox_activated:
            self.current_chatbox.dess()
        else:
            self.current_chatbox = None

            
                
    def take_door(self, x, y):
        for porte in self.portes:
            #retourne une porte selon l'endroit où elle se trouve (sur les côtés ou de haut en bas)
            if not porte.is_in_front:
                if porte.coord['x'] - 5 <= x <= porte.coord['x'] + 5 and porte.coord['y'] <= y <= porte.coord['y'] + porte.size:
                    return porte
            else:
                if porte.coord['x'] <= x <= porte.coord['x'] + porte.size and porte.coord['y'] - 5 <= y <= porte.coord['y'] + 5:
                    return porte
        
        
#création des salles              
Debut = Salle([[260,115,1040,505]], "debut", [])                
Un = Salle([[430, 145, 855, 455], [570, 220, 730, 355], [615, 200, 690, 380]], "1", [Des])                
Deux = Salle( [[385, 170, 925, 470],[330, 205, 425, 415], [500, 201, 588, 425],[550, 225, 760, 425],[720, 201, 800, 420], [880, 140, 975, 220]], "2", [Machine_a_Sous]) 
Quatre = Salle([[380, 65, 920, 550], [455, 215, 650, 405], [740, 60, 850, 440], [900, 60, 925, 345], [415, 275, 455, 340], [645, 270, 675, 345], [700, 70, 740, 135], [700, 145, 740, 210], [700, 220, 785, 300], [700, 295, 740, 350]], "4", [Roulette])
Cinq = Salle([[520, 90, 775, 545], [590, 230, 695, 370], [620, 210, 670, 390]], "5", [])

Fin = Salle( [[260, 120, 1035, 480], [400, 240, 590, 390], [340, 255, 645, 355], [460, 325, 540, 410], [445, 170, 540, 330], [860, 95, 1075, 215],  [855, 175,940, 270], [895, 175, 1055, 305], [940, 305, 1015, 325]],  "fin", []) 
                #mur                 #table droite          #range horizontale   tabouret haut          #tabouret bas       #canapé                 

#création, ajout des portes, ajout des jeux
#salle debut
Porte_D_1 = Porte("D-1", {'x': 260, 'y': 260}, 1000, Un, False, 55) 
Porte_D_2 = Porte("D-2", {'x': 620, 'y': 115}, 1000, Deux, True, 60)
# #Porte_D_3 = Porte("D-3", {'x': 1040, 'y': 300}, 0, salles.Trois)
Porte_D_F = Porte("D-F", {'x': 615, 'y': 505}, 1000000, Fin, True, 60)
Debut.portes.append(Porte_D_1)
Debut.portes.append(Porte_D_2)
Debut.portes.append(Porte_D_F)

Debut.cats.append({"coord": [760, 500], "cat": Greycat_backward()})

#salle 1
Porte_1_D = Porte("1-D", {'x': 855, 'y': 365}, 0, Debut, False, 45)
Porte_1_5 = Porte ("1-5", {'x': 635, 'y': 145}, 10000, Cinq, True, 55)
Un.portes.append(Porte_1_D)
Un.portes.append(Porte_1_5)
Un.cats.append({"coord": [656, 215], "cat": Greycat()})

#salle 2
Porte_2_D = Porte("2-D", {'x': 630, 'y': 470}, 0, Debut, True, 50)
Porte_2_4 = Porte("2-4", {'x': 925, 'y': 300}, 32500, Quatre, False, 50)
Deux.portes.append(Porte_2_D)
Deux.portes.append(Porte_2_4)

Deux.cats.append({"coord": [920, 190], "cat": Greycat()})
Deux.cats.append({"coord": [820, 315], "cat": Greycat()})

from assets.tokens.tokens_opti.token_50 import Token_50
Deux.cats.append({"coord": [920, 190], "cat": Greycat()})
chatbox_miaou = Chatbox(Token_50(), Deux, {}, "Miaou", "MIAOUUOUOUO C FINI UWU UWU UWU UWU MIOAU MIOAU MIOUA MIOUA MOUA MIOU MIOAM IO MIAOU MUAO MOAU")
chatbox_miou = Chatbox(Token_50(), Deux, {1: chatbox_miaou}, "miaou", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

chatbox_demande_caresse = Chatbox(Token_50(), Deux, {2: chatbox_miou, 3: chatbox_miaou}, "MIAOU", "Es-tu un chat ? Je pense que non ? ... Quoi !? tu me dis que tu es un chat ? Mais quel idiotie !!!", "Mais ! Je suis un chat !!!", "Haha ! Tu m'as bien eu!", "MIAAAAAAAAAAAAAAAAAAAOUUUUUUUUUUUUUUUU")
chatbox_demande_caresse.range_x = [875, 925]
chatbox_demande_caresse.range_y = [190,240]

Deux.chatboxes.append(chatbox_demande_caresse)


# Deux.chatboxes.append(Chatbox(Token_50(), Deux, "MIAOU", "Es-tu un chat ? Je pense que non ? ... Quoi !? tu me dis que tu es un chat ? Mais quel idiotie !!!", "Mais ! Je suis un chat !!!", "Haha ! Tu m'as bien eu!", "MIAAAAAAAAAAAAAAAAAAAOUUUUUUUUUUUUUUUU")) #
# Deux.chatboxes.append(Chatbox(Token_50(), Deux, "MIAOU", "Es-tu un chat ? Je pense que non ? ... Quoi !? tu me dis que tu es un chat ? Mais quel idiotie !!!", "Mais ! Je suis un chat !!!", "Haha ! Tu m'as bien eu!", "MIAAAAAAAAAAAAAAAAAAAOUUUUUUUUUUUUUUUU")) #

#salle 3

#salle 4
Porte_4_2 = Porte ("4-2", {'x': 380, 'y': 305}, 0, Deux, False, 30)
Quatre.portes.append(Porte_4_2)

Quatre.cats.append({"coord": [741, 85], "cat": Greycat()})
Quatre.cats.append({"coord": [741, 155], "cat": Greycat()})
Quatre.cats.append({"coord": [742, 285], "cat": Greycat()})
Quatre.cats.append({"coord": [651, 280], "cat": Greycat()})

#salle 5
Porte_5_1 = Porte("5-1", {'x': 640, 'y':545}, 0, Un, True, 25)
Cinq.portes.append(Porte_5_1)

#salle Fin
Porte_F_D = Porte("F-D", {'x': 605, 'y': 120}, 0, Debut, True, 60)
Fin.portes.append(Porte_F_D)
# Porte_F_7 = Porte("F-7", {'x': 1020, 'y': 325}, 0, Debut, False, 30)
#Fin.portes.append(Porte_F_7)

        