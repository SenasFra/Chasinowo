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

Menu_interface = Menu()

class casino:
    def __init__(self):
        pyxel.init(1350, 680, title= "ChasinOwO")
        pyxel.mouse(True)
        self.CHAT = CHAT.CHAT(650,425)
        self.previous_room = None
        self.current_room = salles.Debut
        self.jeux = Menu()
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if self.jeux is None:
            if pyxel.btnp(pyxel.KEY_E):
                #changement de salle            
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
                        
                        
                #lancement d'un jeu
                if len(self.current_room.jeux) != 0:
                    for jeux in self.current_room.jeux:
                        print(self.CHAT.x, self.CHAT.y, jeux.range_x[0], jeux.range_x[1], jeux.range_y[0] , jeux.range_y[1])
                        if jeux.range_x[0] < self.CHAT.x < jeux.range_x[1] and jeux.range_y[0] < self.CHAT.y < jeux.range_y[1]:
                            self.jeux = jeux  
                            self.jeux.jouer = True
                            print(self.jeux)              
                                
            if pyxel.btn(pyxel.KEY_A):
                print(self.CHAT.x, self.CHAT.y, self.CHAT.money, self.CHAT.doors_unlocked, self.jeux)
                    
                    
            self.CHAT.mouv(self.current_room.mur)
            
            if self.current_room == None:
                self.CHAT.mouv(self.salle.mur)
                
        else:
            self.jeux.update()
            if not self.jeux.jouer:
                self.jeux = None 

    def draw(self):
        #si il n'y a pas de jeux lancé, on affiche la salle sinon on affiche le jeu
        if self.jeux is None:
            self.current_room.dess()
            self.CHAT.dess()
        else:
            self.jeux.draw()


running = True
while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    casino()