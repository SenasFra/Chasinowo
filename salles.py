import pyxel
import salles
from games.machine_sous import Machine_a_Sous
from games.des import Des
from games.roulette import Roulette
import porte



class Salle:
    def __init__(self, coord_mur, img_name, jeux):
        self.mur = coord_mur
        self.portes = []
        self.img_name = img_name
        self.jeux = jeux
        
    def dess(self):
        for x in range(6):
            for y in range(4):
                pyxel.image(0).load(0, 0, f"assets/{self.img_name}/{x}{y}.png")
                pyxel.blt(x*225, y*170, 0 ,0, 0, 225, 170)
                
    def take_door(self, x, y):
        for porte in self.portes:
            #retourne une porte selon l'endroit où elle se trouve (sur les côtés ou de haut en bas)
            # if (porte.coord['x'] - 5 <= x < porte.coord['x'] + 5 and porte.coord['y'] < y < porte.coord['y']) + 90 or (porte.coord['x'] < x < porte.coord['x'] + 90 and porte.coord['y'] - 5 <= y < porte.coord['y'] + 5):
            #     return porte
            if not porte.is_in_front:
                if porte.coord['x'] - 5 <= x < porte.coord['x'] + 5 and porte.coord['y'] < y < porte.coord['y'] + porte.size:
                    return porte
            else:
                if porte.coord['x'] < x < porte.coord['x'] + porte.size and porte.coord['y'] - 5 <= y < porte.coord['y'] + 5:
                    return porte
        
        
#création des salles              
Debut = Salle([[270,140,1025,500]], "debut", [])                
Un = Salle([[445, 165, 840, 450], [570, 220, 730, 380], [610, 200, 695, 395]], "1", [Des()])                
Deux = Salle( [[385, 191, 925, 470],[330, 202, 436, 436],[543, 225, 760, 430], [494, 201, 588, 436],[720, 201, 812, 437], [880, 140, 975, 231]], "2", [Machine_a_Sous()]) 
Quatre = Salle([[380, 65, 920, 550], [455, 215, 650, 405], [740, 60, 850, 440], [900, 60, 925, 345], [415, 275, 455, 340], [645, 270, 675, 345], [700, 70, 740, 135], [700, 145, 740, 210], [700, 220, 785, 300], [700, 295, 740, 350]], "4", [Roulette()])
Cinq = Salle([[520, 90, 775, 545], [590, 230, 695, 370], [620, 210, 670, 390]], "5", [])
Fin = Salle( [[270, 145, 1025, 480], [395, 235, 590, 410], [340, 250, 645, 375], [460, 320, 540, 430], [445, 170, 540, 330], [860, 95, 1075, 215], [895, 175, 1055, 325], [840, 175,940,295]], "fin", []) 

#création, ajout des portes, ajout des jeux
#salle debut
Porte_D_1 = porte.Porte("D-1", {'x': 270, 'y': 260}, 1000, Un, False, 55) 
Porte_D_2 = porte.Porte("D-2", {'x': 620, 'y': 140}, 1000, Deux, True, 60)
# #Porte_D_3 = porte.Porte("D-3", {'x': 1025, 'y': 300}, 0, salles.Trois)
Porte_D_F = porte.Porte("D-F", {'x': 615, 'y': 500}, 1000000, Fin, True, 60)
Debut.portes.append(Porte_D_1)
Debut.portes.append(Porte_D_2)
Debut.portes.append(Porte_D_F)

#salle 1
Porte_1_D = porte.Porte("1-D", {'x': 840, 'y': 365}, 0, Debut, False, 45)
Porte_1_5 = porte.Porte ("1-5", {'x': 635, 'y': 165}, 0, Cinq, True, 55)
Un.portes.append(Porte_1_D)
Un.portes.append(Porte_1_5)


#salle 2
Porte_2_D = porte.Porte("2-D", {'x': 630, 'y': 470}, 0, Debut, True, 50)
Porte_2_4 = porte.Porte("2-4", {'x': 925, 'y': 300}, 0, Quatre, False, 50)
Deux.portes.append(Porte_2_D)
Deux.portes.append(Porte_2_4)

#salle 3

#salle 4
Porte_4_2 = porte.Porte ("4-2", {'x': 380, 'y': 305}, 0, Deux, False, 30)
Quatre.portes.append(Porte_4_2)

#salle 5
Porte_5_1 = porte.Porte("5-1", {'x': 640, 'y':545}, 0, Un, True, 25)
Cinq.portes.append(Porte_5_1)

#salle Fin
Porte_F_D = porte.Porte("F-D", {'x': 605, 'y': 145}, 0, Debut, True, 60)
Porte_F_7 = porte.Porte("F-7", {'x': 1025, 'y': 330}, 0, Debut, True, 30)
Fin.portes.append(Porte_F_D)

    
        


# class Fin:
#     def __init__(self):
#         self.mur = [[270, 145, 1025, 480], [395, 235, 590, 410], [340, 250, 645, 375], [460, 320, 540, 430], [445, 170, 540, 330], [860, 95, 1075, 215], [895, 175, 1055, 325], [840, 175,940,295]]
#         self.porte_bas = []
#         self.porte_haut = [590, 680, 145]
#         self.porte_droit = []
#         self.porte_gauche = []
#         self.jeu = []


#     def changer_haut(self):
#         return salles.Debut()

#     def dess(self):
#         for x in range(6):
#             for y in range(4):
#                 pyxel.image(0).load(0, 0, "assets/fin/" + str(x) + str(y) + ".png")
#                 pyxel.blt(x * 225, y * 170, 0, 0, 0, 300, 300)

# class Un:
#     def __init__(self):
#         self.mur = [[445, 165, 840, 450], [570, 220, 730, 380],[610, 200, 695, 395]]
#         self.porte_bas = []
#         self.porte_haut = []
#         self.porte_droit = [840,340,430]
#         self.porte_gauche = []
#         self.jeu = []

#     def changer_droit(self):
#         return salles.Debut()

#     def dess(self):
#         for x in range(6):
#             for y in range(4):
#                 pyxel.image(0).load(0, 0, "assets/1/" + str(x) + str(y) + ".png")
#                 pyxel.blt(x * 225, y * 170, 0, 0, 0, 232, 196)

# class Deux:
#     def __init__(self):
#         self.mur = [[385, 191, 925, 470],[330, 202, 436, 436],[543, 225, 760, 430], [494, 201, 588, 436],[720, 201, 812, 437], [880, 140, 975, 231]]
#         self.porte_bas = [605,695, 470]
#         self.porte_haut = []
#         self.porte_gauche = []
#         self.porte_droit = []
#         self.jeu = [440, 375]

#     def jouer(self):
#         return Des()

#     def changer_bas(self):
#         return salles.Debut()

#     def dess(self):
#         for x in range(6):
#             for y in range(4):
#                 pyxel.image(0).load(0, 0, "assets/2/" + str(x) + str(y) + ".png")
#                 pyxel.blt(x * 225, y * 170, 0, 0, 0, 232, 196)
#         pyxel.image(0).load(0,0,"assets/character/greycat_.png")
#         pyxel.blt(925,191,0,0,0,50,50)
        
        

            