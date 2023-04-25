import pyxel
import time
from assets.font.PyxelUnicode import PyxelUnicode
from timeout import wait

class Chatbox:
    def __init__(self, image, salle, next_chatboxes, nom, question, rep1 = None,rep2 = None,rep3 = None):
        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.range_x = []
        self.range_y = []
        
        self.image_chat = image
        self.salle = salle
        self.next_chatboxes = next_chatboxes
        self.nom_chat = nom
        self.question = question
        self.reponse1 = rep1
        self.reponse2 = rep2
        self.reponse3 = rep3
        self.selected = 0
        
        self.temp = time.time()
            
        if len(self.next_chatboxes) != 0 or rep1 is not None:
            self.selected = 1
        
        
        self.chatbox_activated = True

    def dess(self, porte = None, CHAT = None):
        if self.chatbox_activated:
            pyxel.rect(0,500,1350,430,0) #le cadre de toute la chatbox
            pyxel.rect(0, 500, 1350, 5, 7) #la bande blanche du haut
            
            #si c'est la chatbox d'un chat
            if self.image_chat is not None and self.nom_chat is not None:
                #image du chat
                self.image_chat.dess(0, 376)
                self.font.text(12, 520, self.nom_chat)
                #encadré du nom
                pyxel.rect(20 * len(self.nom_chat),  505,  5,  50,  7)
                pyxel.rect(0,  555,  20 * len(self.nom_chat) + 5,  5,  7)
            
            #la ligne qui partage la question et les réponses
            if self.reponse1 is not None or self.reponse2 is not None or self.reponse3 is not None:
                pyxel.rect(800, 504, 5, 180, 7)
            
            #affichage du texte côté question (celui à gauche)
            if self.reponse1 == None and self.reponse2== None and self.reponse3 == None:
                #il n'y a pas de réponse, le texte prend toute la longueur de la chat box
                if len(self.question) <= 90:
                    self.font.text(20, 600, self.question)
                elif len(self.question) <= 180:
                    self.font.text(20, 570, self.question[:90])
                    if self.question[90] == " ":
                        self.font.text(20, 600, self.question[91:])
                    else:
                        self.font.text(20, 600, self.question[90:])
                else:
                    self.font.text(20, 570, self.question[:90])
                    if self.question[90] == " ":
                        self.font.text(20, 600, self.question[91:180])
                    else:
                        self.font.text(20, 600, self.question[90:180])
                    if self.question[180] == " ":
                        self.font.text(20, 630, self.question[181:])
                    else:
                        self.font.text(20, 630, self.question[180:])
            else:
                #il y a des réponse, le texte s'arrête à la ligne verticale blanche
                if len(self.question) <= 50:
                    self.font.text(20, 600, self.question)
                elif len(self.question) <= 100:
                    self.font.text(20, 570, self.question[:50])
                    if self.question[50] == " ":
                        self.font.text(20, 600, self.question[51:])
                    else:
                        self.font.text(20, 600, self.question[50:])
                else:
                    self.font.text(20, 570, self.question[:50])
                    if self.question[50] == " ":
                        self.font.text(20, 600, self.question[51:100])
                    else:
                        self.font.text(20, 600, self.question[50:100])
                    if self.question[100] == " ":
                        self.font.text(20, 630, self.question[101:])
                    else:
                        self.font.text(20, 630, self.question[100:])
                        
                self.displayArrowAndAnswers()
                    
                self.selectAnswer(pyxel.mouse_x, pyxel.mouse_y)
                
            
            if porte is not None and CHAT is not None:
                self.next_chatbox(pyxel.mouse_x, pyxel.mouse_y, porte, CHAT)
            else:
                self.next_chatbox(pyxel.mouse_x, pyxel.mouse_y)
            
                
    def displayArrowAndAnswers(self):
        #affiche les réponses et la flèche sur la réponse
        #il n'y a qu'une réponse
        if self.reponse1 is not None and self.reponse2 is None and self.reponse3 is None: 
            self.font.text(850,580,self.reponse1)
            pyxel.tri(815,582,815,602,835,592,7) #la fléche est au milieu
            
        #il n'y a que 2 réponse
        if self.reponse1 is not None and self.reponse2 is not None and self.reponse3 is None:
            self.font.text(850,520,self.reponse1)
            self.font.text(850,640,self.reponse2)
            if self.selected == 1:
                pyxel.tri(815,522,815,542,835,532,7) #la flèche est en haut
            else:
                pyxel.tri(815,642,815,662,835,652,7) #la flèche est en bas
                
        #il y a les 3 réponses
        if self.reponse1 is not None and self.reponse2 is not None and self.reponse3 is not None:
            self.font.text(850,520,self.reponse1)
            self.font.text(850,580,self.reponse2)
            self.font.text(850,640,self.reponse3)
            if self.selected == 1:
                pyxel.tri(815,522,815,542,835,532,7) #la fléche est en haut  
            if self.selected == 2:
                pyxel.tri(815,582,815,602,835,592,7) #la flèche est au milieu
            if self.selected == 3:
                pyxel.tri(815,642,815,662,835,652,7) #la flèche est en bas
        
    def selectAnswer(self, x ,y):
        #positionne la flèche sur la réponse selon les touches Z et S
        if pyxel.btnp(pyxel.KEY_Z):
            if self.selected == 2:
                if self.reponse1 is not None:
                    self.selected = 1
            if self.selected == 3:
                if self.reponse2 is not None:
                    self.selected = 2
                elif self.reponse1 is not None:
                    self.selected = 1
                    
        if pyxel.btnp(pyxel.KEY_S):
            if self.selected == 2:
                if self.reponse3 is not None:
                    self.selected = 3
            if self.selected == 1:
                if self.reponse2 is not None:
                    self.selected = 2
                elif self.reponse3 is not None:
                    self.selected = 3       
        
        #positionne la flèche sur la réponse selon le mouvement de la souris et du nombre de réponses affichées
        if 815 <= x <= 1345 and 520 <= y <= 540:    
            if self.reponse1 is not None:
                self.selected = 1    
        if 815 <= x <= 1345 and 580 <= y <= 600 and self.reponse3 is not None:    
            if self.reponse2 is not None:
                self.selected = 2
        if 815 <= x <= 1345 and 640 <= y <= 660:    
            #si il y a 3 réponses choisis la réponse 3
            if self.reponse3 is not None and self.reponse2 is not None:
                self.selected = 3
            #choisi la réponse 2 s'il y en a que 2
            else:
                self.selected = 2
                    
    def next_chatbox(self, x, y, porte = None, CHAT = None):
        
        can_change_chatbox_by_clicking = False
        #change la variable qui permet mettre fin au dialogue actuel
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.reponse1 is self.reponse2 is self.reponse3 is None:
                can_change_chatbox_by_clicking = False
            elif self.reponse2 is None and 815 <= x <= 1345 and 580 <= y <= 600:
                can_change_chatbox_by_clicking = True
            elif self.reponse3 is None and (815 <= x <= 1345 and 520 <= y <= 540 or 815 <= x <= 1345 and 640 <= y <= 660):
                can_change_chatbox_by_clicking = True
            elif (self.reponse2 is not None and self.reponse1 is not None and self.reponse2 is not None) and (815 <= x <= 1345 and 520 <= y <= 540 or 815 <= x <= 1345 and 580 <= y <= 600 or 815 <= x <= 1345 and 640 <= y <= 660):
                can_change_chatbox_by_clicking = True
            
            
        #sélectionne la réponse lorsque l'on clique ou que l'on appuie sur E
        if (pyxel.btnp(pyxel.KEY_E) or can_change_chatbox_by_clicking) and self.wait(0.1):
            #active la prochaine chatbox s'il y en a une et désactive l'actuelle
            if (self.selected != 0 and self.selected in self.next_chatboxes.keys()):
                self.next_chatboxes[self.selected].chatbox_activated = True
                self.salle.current_chatbox = self.next_chatboxes[self.selected]
                
            if porte is not None and CHAT is not None:  
                self.door_bought(porte, CHAT)
                
            self.chatbox_activated = False
            
    def door_bought(self, porte, CHAT):
        #achète la porte
        if self.selected == 1 and self.reponse1 == "Acheter":
            if CHAT.money >= porte.price and CHAT.money >= porte.money_condition:
                print("Acheter ça marche")
                CHAT.money -= porte.price
                CHAT.doors_unlocked.append(porte.name)
                CHAT.doors_unlocked.append(self.door_name_reversed(porte.name))
                return True
            
    def door_name_reversed(self, door_name):
        #renverse le nom d'une porte
        result = ""
        for l in reversed(door_name):
            result += l
        return result
            
    def wait(self, second):
            if time.time() - self.temp < second:
                return False
                
            return True
                    