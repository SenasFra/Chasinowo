import pyxel
import salles
from machine_sous import Machine_a_Sous
from des import Des
import porte


class Salle:
    def __init__(self, coord_mur, portes: list, img_name):
        self.mur = coord_mur
        self.portes = portes
        self.img_name = img_name
        
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
                if porte.coord['x'] - 5 <= x < porte.coord['x'] + 5 and porte.coord['y'] < y < porte.coord['y'] + 90:
                    return porte
            else:
                if porte.coord['x'] < x < porte.coord['x'] + 90 and porte.coord['y'] - 5 <= y < porte.coord['y'] + 5:
                    return porte
        
        
#création des salles              
Debut = Salle([[270,140,1025,500]], [], "debut")                
Un = Salle([[445, 165, 840, 450], [570, 220, 730, 380], [610, 200, 695, 395]], [], "1")                
Deux = Salle( [[385, 191, 925, 470],[330, 202, 436, 436],[543, 225, 760, 430], [494, 201, 588, 436],[720, 201, 812, 437], [880, 140, 975, 231]], [], "2") 
Fin = Salle( [[270, 145, 1025, 480], [395, 235, 590, 410], [340, 250, 645, 375], [460, 320, 540, 430], [445, 170, 540, 330], [860, 95, 1075, 215], [895, 175, 1055, 325], [840, 175,940,295]], [], "fin") 
               

#création et ajout des portes
#salle debut
Porte_D_1 = porte.Porte("D-1", {'x': 270, 'y': 260}, 0, Un, False)
Porte_D_2 = porte.Porte("D-2", {'x': 600, 'y': 140}, 0, Deux, True)
# #Porte_D_3 = porte.Porte("D-3", {'x': 1025, 'y': 300}, 0, salles.Trois)
Porte_D_F = porte.Porte("D-F", {'x': 610, 'y': 500}, 0, Fin, True)
Debut.portes.append(Porte_D_1)
Debut.portes.append(Porte_D_2)
Debut.portes.append(Porte_D_F)

#salle 1
Porte_1_D = porte.Porte("1-D", {'x': 840, 'y': 340}, 0, Debut, False)
Un.portes.append(Porte_1_D)

#salle 2
Porte_2_D = porte.Porte("2-D", {'x': 605, 'y': 470}, 0, Debut, True)
Deux.portes.append(Porte_2_D)

#salle Fin
Porte_F_D = porte.Porte("F-D", {'x': 590, 'y': 145}, 0, Debut, True)
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
        
        

            