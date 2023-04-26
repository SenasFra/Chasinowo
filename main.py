import pyxel
import pygame
import random
import pickle
import os
from assets.font.PyxelUnicode import PyxelUnicode
import salles
import CHAT
from games.machine_sous import Machine_a_Sous
from games.des import Des
from games.roulette import Roulette
from games.blackjack import Blackjack   
from menu import Menu
from intro import Intro
from chatbox import Chatbox
import time
from assets.character.main.gauche import Gauche

from save import save
import atexit

class casino:
    def __init__(self):
        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        pyxel.init(1350, 680, title= "ChasinOwO")
        pyxel.mouse(True)
        #génére la musique
        # random.shuffle(self.musiques)
        # pygame.mixer.music.load("assets/Musiques/" + self.musiques[0])
        # pygame.mixer.music.play()
        
        self.CHAT = CHAT.CHAT(650,425)
        self.previous_room = None
        self.current_room = salles.Un
        self.jeux = None
        
        #variables pour activer et désactiver les dialogues
        self.chatbox_activated = False
        
        #active le bouton E en bas à droite
        self.is_E_button_on = False

        self.porte_triggered = None
        
        pyxel.run(self.update, self.draw)

        
        
    def interface(self):
        # affiche l'interface  
        #contenant l'argent, le bouton sauvegarder
        pyxel.image(0).load(0, 0, "assets/UI/UI_1.png")
        
        pyxel.blt(1205, 20, 0, 0, 0, 138, 157)
        if len(str(self.CHAT.money)) >= 6:
            self.font.text(1275 - 8 * (len(str(self.CHAT.money)) - 1), 50, str(self.CHAT.money))
        else:    
            self.font.text(1275 - 10 * (len(str(self.CHAT.money)) - 1), 50, str(self.CHAT.money))
        #contenant l'inventaire, et le bouton E
        pyxel.image(0).load(0, 0, "assets/UI/UI_2.png")
        pyxel.blt(1205, 400, 0, 0, 0, 138, 237)
        
        #si on est proche d'un objet avec lequel on peut intéragir, on active le bouton E
        if self.is_E_button_on:
            pyxel.image(0).load(0, 0, "assets/UI/E_Button_ON.png")
            pyxel.blt(1225, 518, 0, 0, 0, 100, 100)


    def update(self):
        pyxel.mouse(True)

        #si on a passé le menu (et éventuellement le scénario)
        if self.jeux is None:
            #changement de salle lorsque l'on est proche d'une porte          
            if pyxel.btnp(pyxel.KEY_E) and not self.chatbox_activated and not self.CHAT.assis:
                self.porte_triggered = self.current_room.take_door(self.CHAT.x, self.CHAT.y)
                
                #active la chatbox si le joueur n'a pas débloqué la porte
                if self.porte_triggered is not None and not (self.porte_triggered.name in self.CHAT.doors_unlocked):
                    if self.CHAT.money >= self.porte_triggered.price and self.CHAT.money >= self.porte_triggered.money_condition:
                        door_chatbox = Chatbox(None, self.current_room, {}, None, f"Pour rentrer, il vous faut: acheter la porte      ({self.add_spaces_between_number(self.porte_triggered.price)}$) et avoir {self.add_spaces_between_number(self.porte_triggered.money_condition)}$.", "Acheter", "Annuler")
                    else:
                        door_chatbox = Chatbox(None, self.current_room, {}, None, f"Pour rentrer, il vous faut: acheter la porte      ({self.add_spaces_between_number(self.porte_triggered.price)}$) et avoir {self.add_spaces_between_number(self.porte_triggered.money_condition)}$.", "Annuler")
                    
                    self.active_chatbox(door_chatbox)
                #vérifie si on peut entrer
                if self.porte_triggered is not None:
                    room = self.porte_triggered.enter(self.CHAT)
                    previous_door_name = self.porte_triggered.name

                    #change de salle
                    if room is not None:
                        self.current_room = room
                        #replace le chat
                        new_coord = self.CHAT.replace_cat(self.current_room, previous_door_name)
                        self.CHAT.x, self.CHAT.y = new_coord[0], new_coord[1]
                        save(self.CHAT, self.current_room)
                        
            
            if pyxel.btnp(pyxel.KEY_E) and not self.chatbox_activated:
                #active une chatbox qui n'a pas de rapport avec une porte
                for chatbox in self.current_room.chatboxes:
                    if chatbox.range_x[0] - 5 <= self.CHAT.x <= chatbox.range_x[1] + 5 and chatbox.range_y[0] - 5 <= self.CHAT.y <= chatbox.range_y[1] + 5: #and isinstance(chatbox.nom_chat, chatbox)
                        print("miaou mioua ", self.current_room.current_chatbox)
                        chatbox.temp = time.time()
                        self.active_chatbox(chatbox)
                        
            #permet de sortir du siège           
            if (pyxel.btnp(pyxel.KEY_Z) or pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_S) or pyxel.btnp(pyxel.KEY_D)) and self.CHAT.assis:
                self.CHAT.x, self.CHAT.y = self.CHAT.x-50, self.CHAT.y+40
                self.CHAT.base = Gauche()
                self.CHAT.assis = False
                        
                
                            
            #permet de s'asseoir sur un siège
            #s'assoir sur un siege
            if pyxel.btnp(pyxel.KEY_E):
                if not (self.current_room.siege == []):
                    for elt in self.current_room.siege:
                        if elt[0] < self.CHAT.x < elt[2] and elt[1] < self.CHAT.y < elt[3]:
                            self.CHAT.x, self.CHAT.y = self.current_room.centre_siege(elt)
                            self.CHAT.assis = True
                            
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
                if 1210 <= pyxel.mouse_x <= 1340 and 80 <= pyxel.mouse_y <= 135:
                    save(self.CHAT, self.current_room) 
            
            #le chat peut bouger s'il n'est pas en train de discuter ou qu'il n'est pas assis                    
            if not self.chatbox_activated:       
                self.CHAT.mouv(self.current_room.hitbox)
                
        else:
            #affiche l'interface du jeu        
            self.jeux.update()
            if not self.jeux.jouer:
                #on est dans le menu
                if isinstance(self.jeux, Menu):
                    #récupere la sauvegade
                    if self.jeux.charger:
                        with open('save/data.pickle', 'rb') as f:
                            data = pickle.load(f)
                            self.CHAT.money = data[0]
                            self.CHAT.doors_unlocked = data[1]
                            self.CHAT.x = data[2][0]
                            self.CHAT.y = data[2][1]
                            self.current_room = data[3]
                    else:
                        self.jeux = Intro()        
                                     
                #sauvegarde l'argent gagner
                save(self.CHAT, self.current_room)
                if not self.jeux.jouer:
                    self.jeux = None
                
        

    def draw(self):
        #self.musique()
        #si il n'y a pas de jeux lancé, on affiche la salle sinon on affiche le jeu
        if self.jeux is None:
            self.current_room.dess()
            self.CHAT.dess()
            self.interface() 
            """ gestion des chatbox """
            #il y une chatbox de lancé donc on la dessine
            if self.current_room.current_chatbox is not None and self.current_room.current_chatbox.chatbox_activated:
                #si la chatbox est une porte
                if self.current_room.current_chatbox.reponse1 == "Acheter" and not (self.porte_triggered.name in self.CHAT.doors_unlocked)  and self.porte_triggered != None:
                    self.current_room.current_chatbox.dess(self.porte_triggered, self.CHAT, self.current_room)
                else: 
                    self.current_room.current_chatbox.dess()
                #on a quitté la chatbox
                if not self.current_room.current_chatbox.chatbox_activated:
                    #la chatbox venait d'une porte
                    if self.current_room.current_chatbox.reponse1 == "Acheter":
                            self.porte_triggered = None
                            
            #soit le joueur n'a pas lancé de chatbox soit il en a quitté une
            else:
                self.current_room.current_chatbox = None
                
            #si aucune chatbox est activé, le chat peut bouger (correction du bug: relance la chatbox au moment où on la quitte)
            if self.current_room.current_chatbox is None and self.chatbox_activated:
                self.chatbox_activated = False
        else:
            self.jeux.draw()
            
        
        

    def musique(self):
        if not pygame.mixer.music.get_busy():
            self.musiques.pop(0)
            pygame.mixer.music.load("assets/Musiques/" + self.musiques[0])
            pygame.mixer.music.play()
            if len(self.musiques)==1:
                self.played_music =self.musiques[0]
                self.musiques = os.listdir("assets/Musiques")
                random.shuffle(self.musiques)
                self.musiques.insert(0,self.played_music)
                
    def active_chatbox(self, chatbox):
        self.current_room.current_chatbox = chatbox
        self.current_room.current_chatbox.chatbox_activated = True
        self.chatbox_activated = True
                
   
    def change_E_button_state(self):
        #si le joueur est proche d'un jeu, d'une porte, d'un chat, d'un siège
        for chatbox in self.current_room.chatboxes:
                if chatbox.range_x[0] - 5 <= self.CHAT.x <= chatbox.range_x[1] + 5 and chatbox.range_y[0] - 5 <= self.CHAT.y <= chatbox.range_y[1] + 5:    
                    pass
                
    def add_spaces_between_number(self, number):
        number_str = str(number)
        number_length = len(number_str)
        
        #renvoie directement le nombre si il a moins de 3 chiffres
        if number_length <= 3:
            return number_str
        #si le nombre est un mutliple de 3, calcule le nombre de groupes de 3 chiffres dans celui-ci
        elif number_length % 3 == 0:
            groups_of_3 = number_length // 3
        #de même s'il n'est pas un multiple de 3 sauf qu'on rajoute 1 pour prendre en compte les chiffres restants
        else:
            groups_of_3 = number_length // 3 + 1
            
        space = " "
        result = ""
        
        # Pour chaque groupe de trois chiffres dans le nombre, ajoute un espace et les chiffres à la variable de résultat
        # en partant de la fin du nombre pour traiter les chiffres dans l'ordre correct
        for i in range(groups_of_3):
            start = number_length - (i + 1) * 3
            end = number_length - i * 3
            #si le groupe de 3 traité est plus petit que 3 chiffres, on change la variable à 0 pour prendre en compte les chiffres restants
            if start < 0:
                start = 0
            result = space + number_str[start:end] + result #ajoute un espace et les chiffres du groupe traité
        #supprime les espaces sur les côtés donc celui intiale
        return result.strip()
    
casino()