import pyxel
from games.machine_sous import Machine_a_Sous
from games.des import Des
from games.roulette import Roulette
from porte import Porte
from chatbox import Chatbox
from assets.character.pnj.greycat import Greycat
from assets.character.pnj.greycat_backward import Greycat_backward
from assets.others.plot import plot
from assets.others.chatrpentier import chatrpentier
from assets.tokens.tokens_opti.token_50 import Token_50

class Salle:
    def __init__(self, coord_mur, img_name, jeux):
        self.hitbox = coord_mur
        self.portes = []
        self.img_name = img_name
        self.jeux = jeux
        self.cats = []
        self.plot = []
        self.chatrpentier = []
        self.chatboxes = []
        self.current_chatbox = None
        
    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, f"assets/{self.img_name}/{x}{y}.png")
                pyxel.blt(x*225, y*170, 0 ,0, 0, 225, 170)
        self.Chantier()
        self.Chatrpentier()
        #affiche les chats        
        if len(self.cats) != 0:
            for cat in self.cats:
                cat["cat"].dess(cat["coord"][0], cat["coord"][1])


            
                
    def take_door(self, x, y):
        for porte in self.portes:
            #retourne une porte selon l'endroit où elle se trouve (sur les côtés ou de haut en bas)
            if not porte.is_in_front:
                if porte.coord['x'] - 5 <= x <= porte.coord['x'] + 5 and porte.coord['y'] <= y <= porte.coord['y'] + porte.size:
                    return porte
            else:
                if porte.coord['x'] <= x <= porte.coord['x'] + porte.size and porte.coord['y'] - 5 <= y <= porte.coord['y'] + 5:
                    return porte

    def Chantier(self):
        if len(self.plot) != 0:
            for plot in self.plot:
                plot["plot"].dess(plot["coord"][0],plot["coord"][1])
    def Chatrpentier(self):
        if len(self.chatrpentier) != 0:
            for chatrpentier in self.chatrpentier:
                chatrpentier["chatrpentier"].dess(chatrpentier["coord"][0], chatrpentier["coord"][1])
        
#création des salles              
Debut = Salle([[260,115,1040,505], [730, 460, 800, 510]], "debut", [])
Un = Salle([[430, 145, 855, 455], [570, 220, 730, 355], [615, 180, 690, 380]], "1", [Des])
Deux = Salle( [[385, 170, 925, 470],[330, 205, 425, 415], [500, 201, 588, 425],[550, 225, 760, 425],[720, 201, 800, 420], [880, 140, 975, 220],  [800, 270, 850, 340]], "2", [Machine_a_Sous])
Trois = Salle([[400, 115, 925, 500], [410, 125, 605, 240],[700, 115, 895, 240], [710, 370, 905, 465], [420, 370, 615, 465], [465, 450, 550, 600], [755, 455, 845, 550], [465, 50, 560, 200], [755, 50, 845, 200], [628, 465, 700, 800]], "3", []) # [628, 465, 700, 800] = Plot
Quatre = Salle([[380, 65, 920, 550], [455, 215, 650, 405], [740, 60, 850, 440], [900, 60, 925, 345], [415, 275, 455, 340], [645, 240, 675, 345],[700, 0, 740, 210], [700, 220, 785, 300], [700, 295, 740, 350]], "4", [Roulette])
Cinq = Salle([[520, 90, 775, 545], [590, 230, 695, 370], [620, 210, 670, 390], [697, 425, 800, 475], [520, 385, 775, 440]], "5", [])   #[520, 385, 775, 440] = rangée de plots /// [697, 425, 800, 475] = Chat
Fin = Salle( [[260, 120, 1035, 480], [400, 240, 590, 390], [340, 255, 645, 355], [460, 325, 540, 410], [445, 170, 540, 330], [860, 95, 1075, 215],  [855, 175,940, 270], [895, 175, 1055, 305], [940, 305, 1015, 325]],  "fin", []) 
                #mur                 #table droite          #range horizontale   tabouret haut          #tabouret bas       #canapé                 

#création, ajout des portes, ajout des jeux
#salle debut
Porte_D_1 = Porte("D-1", {'x': 260, 'y': 260}, 1000, Un, False, 55) 
Porte_D_2 = Porte("D-2", {'x': 620, 'y': 115}, 1000, Deux, True, 60)
Porte_D_3 = Porte("D-3", {'x': 1040, 'y': 240}, 0, Trois, False, 100)
Porte_D_F = Porte("D-F", {'x': 615, 'y': 505}, 1000000, Fin, True, 60)
Debut.portes.append(Porte_D_1)
Debut.portes.append(Porte_D_2)
Debut.portes.append(Porte_D_F)
Debut.portes.append(Porte_D_3)
Debut.cats.append({"coord": [760, 500], "cat": Greycat_backward()})

chatbox_vip = Chatbox(Token_50(), Debut, {}, "chat connard", "La porte derriere moi ? C'est pour les plus        riches, les VIP comme moi, allez va-t'en le      pauvre", "s'cuse moi Louis XIV..")

chatbox_vip.range_x = [715, 815]
chatbox_vip.range_y = [455, 505]

Debut.chatboxes.append(chatbox_vip)

#salle 1
Porte_1_D = Porte("1-D", {'x': 855, 'y': 365}, 0, Debut, False, 45)
Porte_1_5 = Porte ("1-5", {'x': 635, 'y': 145}, 10000, Cinq, True, 55)
Un.portes.append(Porte_1_D)
Un.portes.append(Porte_1_5)
Un.cats.append({"coord": [656, 215], "cat": Greycat()})

chatbox_veut_savoir = Chatbox(Token_50(), Un, {}, "Pawtrick", "C'est tres simple ! Tu choisis un nombre ou une   fourchette de nombres puis tu appuies sur ESPACE !", "Merci !")
chatbox_des = Chatbox(Token_50(), Un, {1: chatbox_veut_savoir}, "Pawtrick", "Salut ! Tu veux savoir comment jouer ?", "Avec plaisir !", "Non merci, je connais deja les regles")

chatbox_des.range_x = [595, 715]
chatbox_des.range_y = [195, 260]

Un.chatboxes.append(chatbox_des)

#salle 2
Porte_2_D = Porte("2-D", {'x': 630, 'y': 470}, 0, Debut, True, 50)
Porte_2_4 = Porte("2-4", {'x': 925, 'y': 300}, 32500, Quatre, False, 50)
Deux.portes.append(Porte_2_D)
Deux.portes.append(Porte_2_4)

Deux.cats.append({"coord": [920, 190], "cat": Greycat()})
Deux.cats.append({"coord": [820, 315], "cat": Greycat()})

#mas = machine a sous
chatbox_veut_savoir_mas = Chatbox(Token_50(), Deux, {}, "Whiskette", "Tu vas voir c'est pas dur, il faut glisser les    jetons dans la p'tite encoche puis il te suffit   d'appuyer sur le levier rouge.", "Je vois, merci.")
chatbox_mas = Chatbox(Token_50(), Deux, {1: chatbox_veut_savoir_mas}, "Whiskette", "J'adore ce jeu.. oh salut toi ! Tu veux savoir    comment y jouer ?", "Oui s'il te plait !", "Je sais deja comment y jouer.")

chatbox_mas.range_x = [780, 865]
chatbox_mas.range_y = [260, 370]

Deux.chatboxes.append(chatbox_mas)

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
Porte_3_D = Porte("3-D", {'x': 400, 'y': 275}, 0, Debut, False, 60)
Trois.portes.append(Porte_3_D)
Trois.plot.append({"coord": [661, 500], "plot": plot()})

#salle 4
Porte_4_2 = Porte ("4-2", {'x': 380, 'y': 305}, 0, Deux, False, 30)
Quatre.portes.append(Porte_4_2)

Quatre.cats.append({"coord": [741, 85], "cat": Greycat()})
Quatre.cats.append({"coord": [741, 155], "cat": Greycat()})
Quatre.cats.append({"coord": [742, 285], "cat": Greycat()})
Quatre.cats.append({"coord": [651, 280], "cat": Greycat()})


chatbox_lait1 = Chatbox(Token_50(), Quatre, {}, "Ronron", "Wouahh comment il est trop bon ce lait au raisin !", "Mhm chat donne envie !")

chatbox_lait1.range_x = [670, 695]
chatbox_lait1.range_y = [65, 110]

chatbox_lait2 = Chatbox(Token_50(), Quatre, {}, "Patoune", "J'vois tout flou, j'ai pris trrrrop d'laaaait  au rhum ! *hoquete*", "Oula..")

chatbox_lait2.range_x = [670, 695]
chatbox_lait2.range_y = [145, 200]

chatbox_lait3_1 = Chatbox(Token_50(), Quatre, {}, "Purrcival", "Un... un chatellite ! Hahaha ! Comme un satellite, mais avec chat dedans ! *glousse* T'as compris,  hein ? Hahaha ! C'est trop... trop drole ! Non ?", "Ahah, ouais c'est ca...")
chatbox_lait3_2 = Chatbox(Token_50(), Quatre, {}, "Purrcival", "*hic* Dommage *vous regarde d'un air aneanti*")
chatbox_lait3 = Chatbox(Token_50(), Quatre, {1: chatbox_lait3_1, 2: chatbox_lait3_2}, "Purrcival", "Alors, attends... attends... j'ai une blague pour toi ! Tu sais ce qu'est un chat dans l'espace ?   *hoquete*", "Non, je sais pas...", "Laisse moi tranquille")

chatbox_lait3.range_x = [725, 800]
chatbox_lait3.range_y = [330, 365]


chatbox_veut_savoir_roulette = Chatbox(Token_50(), Quatre, {}, "Chatlyn", "D'abord tu places un jeton ou tu le souhaites sur le plateau, ensuite tu cliques sur la roulette.   Aussi simple que chat !", "D'accord !")
chatbox_roulette = Chatbox(Token_50(), Quatre, {1: chatbox_veut_savoir_roulette}, "Chatlyn", "Coucou mon chat, tu veux savoir comment on joue ?", "Oui !", "Je sais deja comment y jouer.")

chatbox_roulette.range_x = [635, 695]
chatbox_roulette.range_y = [210, 360]

Quatre.chatboxes.append(chatbox_roulette)
Quatre.chatboxes.append(chatbox_lait1)
Quatre.chatboxes.append(chatbox_lait2)
Quatre.chatboxes.append(chatbox_lait3)

#salle 5
Porte_5_1 = Porte("5-1", {'x': 640, 'y':545}, 0, Un, True, 25)
Cinq.portes.append(Porte_5_1)

Cinq.plot.append({"coord": [520, 430], "plot": plot()})
Cinq.plot.append({"coord": [570, 430], "plot": plot()})
Cinq.plot.append({"coord": [620, 430], "plot": plot()})
Cinq.plot.append({"coord": [670, 430], "plot": plot()})
Cinq.plot.append({"coord": [720, 430], "plot": plot()})
Cinq.plot.append({"coord": [770, 430], "plot": plot()})
Cinq.plot.append({"coord": [543, 118], "plot": plot()})
Cinq.plot.append({"coord": [629, 199], "plot": plot()})
Cinq.plot.append({"coord": [772, 138], "plot": plot()})
Cinq.plot.append({"coord": [744, 289], "plot": plot()})
Cinq.chatrpentier.append({"coord": [738, 450] , "chatrpentier": chatrpentier()})
Cinq.chatrpentier.append({"coord": [629, 135] , "chatrpentier": chatrpentier()})

chatbox_travaux = Chatbox(Token_50(), Cinq, {}, "Chatrpentier", "Miaou ! C'est en travaux, repasse plus tard !", "miaou, ok")
chatbox_travaux.range_x = [697, 777]
chatbox_travaux.range_y = [445, 495]

Cinq.chatboxes.append(chatbox_travaux)

#salle Fin
Porte_F_D = Porte("F-D", {'x': 605, 'y': 120}, 0, Debut, True, 60)
Fin.portes.append(Porte_F_D)
# Porte_F_7 = Porte("F-7", {'x': 1020, 'y': 325}, 0, Debut, False, 30)
#Fin.portes.append(Porte_F_7)

        