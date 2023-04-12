import pyxel
import salles
import CHAT
#import pygame
from games.machine_sous import Machine_a_Sous
from games.des import Des
from menu import Menu

# pygame.init()
# pygame.mixer.music.load("assets/Musiques/Nouveau_projet.mp3")
#pygame.mixer.music.play(-1)

class casino:
    def __init__(self):
        pyxel.init(1350, 680, title= "ChasinOwO")
        pyxel.mouse(True)
        self.CHAT = CHAT.CHAT(650,425)
        self.previous_room = None
        self.current_room = salles.Debut
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_E):            
            porte = self.current_room.take_door(self.CHAT.x, self.CHAT.y)
            #vérifie si on peut entrer
            if porte is not None:
                room = porte.enter(self.CHAT)
                previous_door_name = porte.name
                #change de salle
                if room is not None:
                    self.current_room = room
                    #replace le chat
                    new_coord = self.CHAT.replace_cat(self.current_room, previous_door_name)
                    self.CHAT.x, self.CHAT.y = new_coord[0], new_coord[1]

                            
        if pyxel.btn(pyxel.KEY_A):
            print(self.CHAT.x, self.CHAT.y, self.CHAT.money, self.CHAT.doors_unlocked)
                
                
        self.CHAT.mouv(self.current_room.mur)
        
        if self.current_room == None:
            self.CHAT.mouv(self.salle.mur)
        #     if len(self.salle.porte_bas)==3:
        #         if self.perso.x >= self.salle.porte_bas[0] and self.perso.x <= self.salle.porte_bas[1] and self.perso.y == self.salle.porte_bas[2] and pyxel.btnp(pyxel.KEY_E):
        #             self.salle = self.salle.changer_bas()
        #             self.perso.x = (self.salle.porte_haut[0] + self.salle.porte_haut[1])//2
        #             self.perso.y = self.salle.mur[0][1]+5
        #     if len(self.salle.porte_haut)==3:
        #         if self.perso.x >= self.salle.porte_haut[0] and self.perso.x <= self.salle.porte_haut[1] and self.perso.y == self.salle.porte_haut[2] and pyxel.btnp(pyxel.KEY_E):
        #             self.salle = self.salle.changer_haut()
        #             self.perso.x = (self.salle.porte_bas[0] + self.salle.porte_bas[1])//2
        #             self.perso.y = self.salle.mur[0][3]-5
        #     if len(self.salle.porte_droit)==3:
        #         if self.perso.y >= self.salle.porte_droit[1] and self.perso.y <= self.salle.porte_droit[2] and self.perso.x == self.salle.porte_droit[0] and pyxel.btnp(pyxel.KEY_E):
        #             self.salle = self.salle.changer_droit()
        #             self.perso.x = self.salle.porte_gauche[0]+5
        #             self.perso.y = (self.salle.porte_gauche[1] + self.salle.porte_gauche[2])//2
        #     if len(self.salle.porte_gauche)==3:
        #         if self.perso.y >= self.salle.porte_gauche[1] and self.perso.y <= self.salle.porte_gauche[2] and self.perso.x == self.salle.porte_gauche[0] and pyxel.btnp(pyxel.KEY_E):
        #             self.salle = self.salle.changer_gauche()
        #             self.perso.x = self.salle.porte_droit[0] - 5
        #             self.perso.y = (self.salle.porte_droit[1] + self.salle.porte_droit[2]) // 2
        #     if pyxel.btnp(pyxel.KEY_E):
        #         if len(self.salle.jeu)==2:
        #             if self.perso.x >= self.salle.jeu[0] and self.perso.x <= self.salle.jeu[0]+75 and self.perso.y >= self.salle.jeu[1] and self.perso.y <= self.salle.jeu[1]+75:
        #                 self.jeu = self.salle.jouer()
        #     if pyxel.btnp(pyxel.KEY_K):
        #         print(self.perso.x,self.perso.y)
        # else:
        #     self.jeu.update()

    def draw(self):
        self.current_room.dess()
        self.CHAT.dess()


running = True
while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    casino()