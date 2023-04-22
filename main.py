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
        self.current_room = salles.Deux
        self.jeux = Machine_a_Sous(self.CHAT)
        pyxel.run(self.update, self.draw)
        
    def interface(self):
        # affiche l'argent
        pyxel.text(1210, 20, "ARGENT:", 7)
        pyxel.text(1210, 40, str(self.CHAT.money), 7)
        

    def update(self):
        pyxel.mouse(True)
        #si on a passé le menu (et éventuellement le scénario)
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
                        temp = jeux(self.CHAT)  
                        if temp.range_x[0] < self.CHAT.x < temp.range_x[1] and temp.range_y[0] < self.CHAT.y < temp.range_y[1]:
                            self.jeux = temp
                            self.jeux.jouer = True
                                
            if pyxel.btn(pyxel.KEY_A):
                print(self.CHAT.x, self.CHAT.y, self.CHAT.money, self.CHAT.doors_unlocked, self.jeux)
            
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                print(pyxel.mouse_x, pyxel.mouse_y)
                    
            self.CHAT.mouv(self.current_room.mur)
            
            
            # if self.current_room == None:
            #     self.CHAT.mouv(self.salle.mur)
                
        else:
            self.jeux.update()
            if not self.jeux.jouer:
                self.jeux = None 

    def draw(self):
        #si il n'y a pas de jeux lancé, on affiche la salle sinon on affiche le jeu
        if self.jeux is None:
            self.current_room.dess()
            self.CHAT.dess()
            self.interface() 
        else:
            self.jeux.draw()


running = True
while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    casino()