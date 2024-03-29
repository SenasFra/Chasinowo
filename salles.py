import pyxel
from games.machine_sous import Machine_a_Sous
from games.des import Des
from games.roulette import Roulette
from games.blackjack import Blackjack
from porte import Porte
from chatbox import Chatbox
from assets.character.pnj.greycat import Greycat
from assets.character.pnj.greycat_backward import Greycat_backward
from assets.others.plot import plot
from assets.others.chatrpentier import chatrpentier
from assets.tokens.tokens_opti.token_50 import Token_50


from assets.character.pnj.lunettes import Lunettes
from assets.character.pnj.orange_cat import Orange_Cat
from assets.character.pnj.blue_cat import Blue_Cat
from assets.character.pnj.yellow_cat import Yellow_Cat
from assets.character.pnj.mainly_white_cat import Mainly_White_Cat
from assets.character.pnj.colorful_cat import Colorful_Cat
from assets.character.pnj.chattarde import Chattarde
from assets.character.pnj.cheisenberg import Cheisenberg

from assets.character.pnj.pnjheads.grey_head import Grey_Head
from assets.character.pnj.pnjheads.lunettes_head import Lunettes_Head
from assets.character.pnj.pnjheads.orange_head import Orange_Head
from assets.character.pnj.pnjheads.blue_head import Blue_Head
from assets.character.pnj.pnjheads.yellow_head import Yellow_Head
from assets.character.pnj.pnjheads.mainly_white_head import Mainly_White_Head
from assets.character.pnj.pnjheads.colorful_head import Colorful_Head
from assets.character.pnj.pnjheads.chattarde_head import Chattarde_Head
from assets.others.charpentier_head import Charpentier_Head


class Salle:
    def __init__(self, coords_hitbox: list, img_name: object, jeux: object, sieges: list):
        self.hitbox = coords_hitbox
        self.portes = []
        self.img_name = img_name
        self.jeux = jeux
        self.cats = []
        self.plots = []
        self.chatrpentiers = []
        self.chatboxes = []
        self.siege = sieges
        self.current_chatbox = None
        
    def dess(self):
        #affiche la salle
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, f"assets/{self.img_name}/{x}{y}.png")
                pyxel.blt(x*225, y*170, 0 ,0, 0, 225, 170)
                
        #si il y a des travaux
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
                
    def centre_siege(self, elt):
        return (elt[0] + elt[2]) // 2, (elt[1] + elt[3]) // 2

    def Chantier(self):
        #génère les plots
        if len(self.plots) != 0:
            for plot in self.plots:
                plot["plot"].dess(plot["coord"][0],plot["coord"][1])
                
    def Chatrpentier(self):
        #génère les chatrpentiers
        if len(self.chatrpentiers) != 0:
            for chatrpentier in self.chatrpentiers:
                chatrpentier["chatrpentier"].dess(chatrpentier["coord"][0], chatrpentier["coord"][1])
        
#création des salles              
Debut = Salle([[260,115,1040,505], [730, 460, 800, 510], [620, 330, 690, 385]], "debut", [], [])
                #mur                # chat vip           ##chat coloré
Un = Salle([[430, 145, 855, 455], [570, 225, 730, 350], [615, 180, 700, 225], [620, 345, 690, 380]], "1", [Des], [])
Deux = Salle( [[385, 170, 925, 470], [330, 205, 425, 415], [500, 201, 588, 425],[550, 225, 760, 425],[720, 201, 800, 420], [880, 140, 975, 220],  [800, 270, 850, 340]], "2", [Machine_a_Sous], [])
Trois = Salle([[400, 115, 925, 500], [410, 125, 605, 240],[700, 115, 895, 240], [710, 370, 905, 465], [420, 370, 615, 465], [465, 450, 550, 600], [755, 455, 845, 550], [465, 50, 560, 200], [755, 50, 845, 200], [628, 465, 700, 800], [710, 330, 780, 380], [840, 330, 910, 380]], "3", [Blackjack], []) # [628, 465, 700, 800] = Plot
Quatre = Salle([[380, 65, 920, 550], [455, 215, 650, 405], [740, 60, 850, 440], [900, 60, 925, 345], [415, 275, 455, 340], [645, 240, 675, 345],[700, 0, 740, 210], [700, 220, 785, 300], [700, 295, 740, 350]], "4", [Roulette], [[690, 180, 785, 260]])
Cinq = Salle([[515, 90, 775, 545], [590, 230, 695, 370], [620, 210, 670, 390], [700, 425, 800, 495], [510, 385, 775, 440]], "5", [], [])   #[520, 385, 775, 440] = rangée de plots /// [700, 425, 800, 475] = Chat
Fin = Salle( [[260, 120, 1035, 480], [400, 240, 590, 390], [340, 255, 645, 355], [460, 325, 540, 410], [445, 170, 540, 330], [860, 95, 1075, 215],  [855, 175,940, 270], [895, 175, 1055, 305], [940, 305, 1015, 325]],  "fin", [], [[450, 280, 550, 420], [920, 180, 1040, 350]])

"""salle debut"""
#les portes
Porte_D_1 = Porte("D-1", {'x': 260, 'y': 260}, 1000, 2000, Un, False, 55) 
Porte_D_2 = Porte("D-2", {'x': 620, 'y': 115}, 1000, 2000, Deux, True, 60)
Porte_D_3 = Porte("D-3", {'x': 1040, 'y': 240}, 0, 0, Trois, False, 100)
Porte_D_F = Porte("D-F", {'x': 615, 'y': 505}, 1000000, 1010000, Fin, True, 60)
Debut.portes.append(Porte_D_1)
Debut.portes.append(Porte_D_2)
Debut.portes.append(Porte_D_F)
Debut.portes.append(Porte_D_3)

#ajout de chats
Debut.cats.append({"coord": [655, 370], "cat": Colorful_Cat()})
Debut.cats.append({"coord": [760, 500], "cat": Greycat_backward()})


#ajout de dialogue
chatbox_vip = Chatbox(Grey_Head(), Debut, {}, "Persan", "La porte derriere moi ? C'est pour les plus        riches, les VIP comme moi, allez va-t'en le      pauvre", "s'cuse moi Louis XIV..")
chatbox_vip.range_x = [715, 815]
chatbox_vip.range_y = [455, 505]
Debut.chatboxes.append(chatbox_vip)

chatboxa = Chatbox(Colorful_Head(), Debut, {}, "Zongo", "Avant que j'oublie ! Pour quitter un jeu, appuie sur A et surtout pas  sur echap !!!", "Merci !")
chatbox_d_oui_2 = Chatbox(Colorful_Head(), Debut, {1 : chatboxa}, "Zongo", "Tu vas en choisir une des deux, la debloquer puis la passer, et tu auras acces a ton premier jeu !", "continuer")
chatbox_d_oui = Chatbox(Colorful_Head(), Debut, {1 : chatbox_d_oui_2}, "Zongo", "D'accord ! Je vais t'expliquer, tu vois les portes en haut et a gauche ?", "continuer")
chatbox_debut = Chatbox(Colorful_Head(), Debut, {1 : chatbox_d_oui}, "Zongo", "Coucou, t'es nouveau ici toi ?", "Oui.", "Non.")

chatbox_debut.range_x = [600, 700]
chatbox_debut.range_y = [320, 385]
Debut.chatboxes.append(chatbox_debut)
"""salle 1"""
#les portes
Porte_1_D = Porte("1-D", {'x': 855, 'y': 365}, 0, 0, Debut, False, 45)
Porte_1_5 = Porte ("1-5", {'x': 635, 'y': 145}, 0, 0, Cinq, True, 55)
Un.portes.append(Porte_1_D)
Un.portes.append(Porte_1_5)

#ajout d'un chat
Un.cats.append({"coord": [656, 215], "cat": Lunettes()})

#ajout de dialogue
chatbox_veut_savoir = Chatbox(Lunettes_Head(), Un, {}, "Pawtrick", "C'est tres simple ! Tu choisis un nombre ou une   fourchette de nombres puis tu appuies sur ESPACE !", "Merci !")
chatbox_des = Chatbox(Lunettes_Head(), Un, {1: chatbox_veut_savoir}, "Pawtrick", "Salut ! Tu veux savoir comment jouer ?", "Avec plaisir !", "Non merci, je connais deja les regles")

chatbox_des.range_x = [595, 715]
chatbox_des.range_y = [170, 260]

Un.chatboxes.append(chatbox_des)

"""salle 2"""
#les portes
Porte_2_D = Porte("2-D", {'x': 630, 'y': 470}, 0, 0, Debut, True, 50)
Porte_2_4 = Porte("2-4", {'x': 925, 'y': 300}, 12500, 32000, Quatre, False, 50)
Deux.portes.append(Porte_2_D)
Deux.portes.append(Porte_2_4)

#ajout de chats
Deux.cats.append({"coord": [920, 190], "cat": Greycat()})
Deux.cats.append({"coord": [820, 315], "cat": Orange_Cat()})

#ajout de dialogues
#mas = machine a sous
chatbox_veut_savoir_mas = Chatbox(Orange_Head(), Deux, {}, "Whiskette", "Tu vas voir c'est pas dur, il faut glisser les    jetons dans la p'tite encoche puis il te suffit   d'appuyer sur le levier rouge.", "Je vois, merci.")
chatbox_mas = Chatbox(Orange_Head(), Deux, {1: chatbox_veut_savoir_mas}, "Whiskette", "J'adore ce jeu.. oh salut toi ! Tu veux savoir    comment y jouer ?", "Oui s'il te plait !", "Je sais deja comment y jouer.")

chatbox_mas.range_x = [780, 865]
chatbox_mas.range_y = [260, 370]

Deux.chatboxes.append(chatbox_mas)

Deux.cats.append({"coord": [920, 190], "cat": Greycat()})
#test des 1eres chatbox
# chatbox_miaou = Chatbox(Grey_Head(), Deux, {}, "Miaou", "MIAOUUOUOUO C FINI UWU UWU UWU UWU MIOAU MIOAU MIOUA MIOUA MOUA MIOU MIOAM IO MIAOU MUAO MOAU")
# chatbox_miou = Chatbox(Grey_Head(), Deux, {1: chatbox_miaou}, "miaou", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# chatbox_demande_caresse = Chatbox(Grey_Head(), Deux, {2: chatbox_miou, 3: chatbox_miaou}, "MIAOU", "Es-tu un chat ? Je pense que non ? ... Quoi !? tu me dis que tu es un chat ? Mais quel idiotie !!!", "Mais ! Je suis un chat !!!", "Haha ! Tu m'as bien eu!", "MIAAAAAAAAAAAAAAAAAAAOUUUUUUUUUUUUUUUU")
# chatbox_demande_caresse.range_x = [875, 925]
# chatbox_demande_caresse.range_y = [190,240]

# Deux.chatboxes.append(chatbox_demande_caresse)

"""salle 3"""
#ajout d'un porte
Porte_3_D = Porte("3-D", {'x': 400, 'y': 275}, 0, 0, Debut, False, 60)
Trois.portes.append(Porte_3_D)

#ajout de chats
Trois.cats.append({"coord": [517, 110], "cat": Yellow_Cat()})
Trois.cats.append({"coord": [458, 190], "cat": Greycat()})
Trois.cats.append({"coord": [565, 190], "cat": Mainly_White_Cat()})
Trois.cats.append({"coord": [806, 108], "cat": Colorful_Cat()})
Trois.cats.append({"coord": [808, 453], "cat": Lunettes()})
Trois.cats.append({"coord": [747, 376], "cat": Orange_Cat()})
Trois.cats.append({"coord": [511, 458], "cat": Blue_Cat()})
Trois.cats.append({"coord": [747, 187], "cat": Blue_Cat()})
Trois.cats.append({"coord": [855, 187], "cat": Orange_Cat()})
Trois.cats.append({"coord": [871, 375], "cat": Mainly_White_Cat()})

#ajout d'un plot
Trois.plots.append({"coord": [661, 500], "plot": plot()})

"""salle 4"""
#ajout d'un porte
Porte_4_2 = Porte ("4-2", {'x': 380, 'y': 305}, 0, 0, Deux, False, 30)
Quatre.portes.append(Porte_4_2)

#ajout de chats
Quatre.cats.append({"coord": [741, 85], "cat": Yellow_Cat()})
Quatre.cats.append({"coord": [741, 155], "cat": Blue_Cat()})
Quatre.cats.append({"coord": [742, 285], "cat": Mainly_White_Cat()})
Quatre.cats.append({"coord": [651, 280], "cat": Colorful_Cat()})

#ajout des dialogues
chatbox_lait1 = Chatbox(Yellow_Head(), Quatre, {}, "Ronron", "Wouahh comment il est trop bon ce lait au raisin !", "Mhm chat donne envie !")

chatbox_lait1.range_x = [670, 695]
chatbox_lait1.range_y = [65, 110]

chatbox_lait2 = Chatbox(Blue_Head(), Quatre, {}, "Patoune", "J'vois tout flou, j'ai pris trrrrop d'laaaait  au rhum ! *hoquete*", "Oula..")

chatbox_lait2.range_x = [670, 695]
chatbox_lait2.range_y = [145, 200]

chatbox_lait3_1 = Chatbox(Mainly_White_Head(), Quatre, {}, "Purrcival", "Un... un chatellite ! Hahaha ! Comme un satellite, mais avec chat dedans ! *glousse* T'as compris,  hein ? Hahaha ! C'est trop... trop drole ! Non ?", "Ahah, ouais c'est ca...")
chatbox_lait3_2 = Chatbox(Mainly_White_Head(), Quatre, {}, "Purrcival", "*hic* Dommage *vous regarde d'un air aneanti*")
chatbox_lait3 = Chatbox(Mainly_White_Head(), Quatre, {1: chatbox_lait3_1, 2: chatbox_lait3_2}, "Purrcival", "Alors, attends... attends... j'ai une blague pour toi ! Tu sais ce qu'est un chat dans l'espace ?   *hoquete*", "Non, je sais pas...", "Laisse moi tranquille")

chatbox_lait3.range_x = [725, 800]
chatbox_lait3.range_y = [330, 365]

chatbox_veut_savoir_jetons = Chatbox(Colorful_Head(), Quatre, {}, "Chatlyn", "Pour les jetons, ils coutent 10 000 fois leur     valeur. Par exemple le jeton 1 coute 10 000 $w$.", "D'accord !")
chatbox_veut_savoir_roulette = Chatbox(Colorful_Head(), Quatre, {1: chatbox_veut_savoir_jetons}, "Chatlyn", "D'abord tu places un jeton ou tu le souhaites sur le plateau, ensuite tu cliques sur la roulette.   Aussi simple que chat !", "Et les valeurs des jetons ?")
chatbox_roulette = Chatbox(Colorful_Head(), Quatre, {1: chatbox_veut_savoir_roulette}, "Chatlyn", "Coucou mon chat, tu veux savoir comment on joue ?", "Oui !", "Je sais deja comment y jouer.")

chatbox_roulette.range_x = [635, 685]
chatbox_roulette.range_y = [210, 360]

Quatre.chatboxes.append(chatbox_roulette)
Quatre.chatboxes.append(chatbox_lait1)
Quatre.chatboxes.append(chatbox_lait2)
Quatre.chatboxes.append(chatbox_lait3)

"""salle 5"""
#ajout d'une porte
Porte_5_1 = Porte("5-1", {'x': 640, 'y':545}, 0, 0, Un, True, 25)
Cinq.portes.append(Porte_5_1)

#ajout du chantier (plots + chatrpentiers)
Cinq.plots.append({"coord": [520, 430], "plot": plot()})
Cinq.plots.append({"coord": [570, 430], "plot": plot()})
Cinq.plots.append({"coord": [620, 430], "plot": plot()})
Cinq.plots.append({"coord": [670, 430], "plot": plot()})
Cinq.plots.append({"coord": [720, 430], "plot": plot()})
Cinq.plots.append({"coord": [770, 430], "plot": plot()})
Cinq.plots.append({"coord": [543, 118], "plot": plot()})
Cinq.plots.append({"coord": [629, 199], "plot": plot()})
Cinq.plots.append({"coord": [772, 138], "plot": plot()})
Cinq.plots.append({"coord": [744, 289], "plot": plot()})
Cinq.chatrpentiers.append({"coord": [738, 450] , "chatrpentier": chatrpentier()}) #chatrpentier en bas là
Cinq.chatrpentiers.append({"coord": [629, 135] , "chatrpentier": chatrpentier()}) #chatrpentier en haut

#ajout d'un dialogue
#rmplacer par chatrpentier_head
chatbox_travaux = Chatbox(Charpentier_Head(), Cinq, {}, "Chatrpentier", "Miaou ! C'est en travaux, repasse plus tard !", "miaou, ok")
chatbox_travaux.range_x = [697, 777]
chatbox_travaux.range_y = [445, 495]

Cinq.chatboxes.append(chatbox_travaux)

"""salle Fin"""
#ajout d'une porte
Porte_F_D = Porte("F-D", {'x': 605, 'y': 120}, 0, 0, Debut, True, 60)
Fin.portes.append(Porte_F_D)

#ajout des chats

#ajout des dialogues
fin_jeu = Chatbox(None, Fin, {}, None, "Bravo mon chat, tu as fini le jeu, il n'est pas encore termine mais j'espere que ca t'a   plu, n'hesite pas a depenser tout ton argent maintenant.")
Fin.current_chatbox = fin_jeu

#ajout d'un plot
Fin.plots.append({"coord": [1070, 315], "plot": plot()})


