import pyxel
import time
from random import randint
from assets.font.PyxelUnicode import PyxelUnicode
from assets.tokens.tokens_opti.token_1 import Token_1
from assets.tokens.tokens_opti.token_2 import Token_2
from assets.tokens.tokens_opti.token_5 import Token_5
from assets.tokens.tokens_opti.token_10 import Token_10
from assets.tokens.tokens_opti.token_20 import Token_20
from assets.tokens.tokens_opti.token_50 import Token_50
import math

class Machine_a_Sous:
    def __init__(self, CHAT):
        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.font_token_value = PyxelUnicode("assets/font/pixelmix.ttf", 12)
        
        self.range_x = [380, 455]
        self.range_y = [370, 450]
        self.x = 450
        self.y = 145
        
        self.proba_chat7 = 0.5
        self.proba_chat_citron_casque = 0.25
        self.proba_chat_orange = 0.2
        self.proba_chat_bar = 0.05
        
        self.token_1 = Token_1()
        self.token_2 = Token_2()
        self.token_5 = Token_5()
        self.token_10 = Token_10()
        self.token_20 = Token_20()
        self.token_50 = Token_50()
        self.token_x = 100
        self.token_y = 145
        self.tokens = {1: self.token_1, 2: self.token_2, 5: self.token_5, 10: self.token_10, 20: self.token_20, 50: self.token_50}
        self.token_value = {1: 100, 2: 200, 5: 500, 10: 1000, 20: 2000, 50: 5000}
        self.token_taken = 0
        
        self.results_name = ["", "", ""]
        self.results_number = [0, 0, 0]

        self.jouer = True
        self.CHAT = CHAT
        self.mise = 0
        self.can_play = True
        self.frames_counter = 0 #sert de compteur pour afficher l'argent gagné après que les résultats ont été affichés
        
    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.jouer = False
            
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            #prend un jeton
            if self.token_x <= x <= self.token_x + 40 and self.token_y <= y <= self.token_y + 50 * 6:
                self.takeToken(y)
            #place le jeton dans l'encoche
            if self.x + 200 <= x <= self.x + 600 and self.y + 480 <= y <= self.y + 515 and self.token_taken != 0:
                self.place_token_in_game()
                
            #lance le jeu    
            if self.x + 809 <= x <= self.x + 849 and self.y + 104 <= y <= self.y + 144 and self.mise > 0:
                self.play()

    def draw(self):
        pyxel.cls(5)
        self.affichage()
        #affiche l'image des résultat les unes après les autres
        if self.frames_counter < 3 and self.can_play == False:
            pyxel.mouse(False)
            if self.frames_counter == -1:
                self.draw_empty_cases()
            else:
                self.display_n_results(self.frames_counter + 1)
                time.sleep(1)
            self.frames_counter += 1
        else:
            self.display_n_results(3)
            
        if self.frames_counter == 3:
            self.update_money()
        
    def display_n_results(self, n):
        for k in range(n):
            if self.results_name[k] != "":
                pyxel.image(0).load(0, 0, f"assets/Machine_sous/{self.results_name[k]}.png")
                pyxel.blt(self.x+80 + 220 * k, self.y+100, 0, 0, 0, 200, 200)

    def display_tokens(self):
        k = 0
        #parcours la liste des jetons et appelle la fonction qui permet de les afficher
        for n, token in self.tokens.items():
            token.dess(self.token_x,  self.token_y + 50 * k)
            self.font_token_value.text(self.token_x + 40 + 10, self.token_y + 15 + (40 * 1.25) * k, str(self.token_value[n]))
            k+=1
            
    def takeToken(self, y):
        size = 40
        gap = 10
        #jeton 1
        if self.y <= y <= self.y + size and self.CHAT.money >= 100:
            self.token_taken = 1
        #jeton 2
        elif self.y + (size + gap) <= y <= self.y + 2 * size + gap and self.CHAT.money >= 200:
            self.token_taken = 2
        #jeton 5
        elif self.y + 2 * (size + gap) <= y <= self.y + 3 * size + 2 * gap and self.CHAT.money >= 500:
            self.token_taken = 5
        #jeton 10
        elif self.y + 3 * (size + gap) <= y <= self.y + 4 * size + 3 * gap and self.CHAT.money >= 1000:
            self.token_taken = 10
        #jeton 20
        elif self.y + 4 * (size + gap) <= y <= self.y + 5 * size + 4 * gap and self.CHAT.money >= 2000:
            self.token_taken = 20
        #jeton 50
        elif self.y + 5 * (size + gap) <= y <= self.y + 6 * size + 5 *gap and self.CHAT.money >= 5000:
            self.token_taken = 50
        else:
            self.token_taken = 0
            
    def place_token_in_game(self):
        #augmente la mise selon le jeotn insérer
        self.mise += self.token_value[self.token_taken]
        self.CHAT.money -= self.token_value[self.token_taken]
        self.token_taken = 0
            

    def affichage(self):
        self.money_taker()
        self.machine()
        self.display_money_bar()
        self.display_tokens()
        self.cursor(pyxel.mouse_x, pyxel.mouse_y)
        
    def cursor(self, x, y):
        if self.token_taken != 0:
            self.tokens[self.token_taken].dess(x - 20, y - 20)
        
    def display_money_bar(self):
        # la barre
        pyxel.rect(self.x+280,self.y-20,20,20,3)
        pyxel.rect(self.x+500,self.y-20,20,20,3)
        pyxel.rect(self.x+20,self.y-100,760,80,3)
        pyxel.circ(self.x+20,self.y-80,20,3)
        pyxel.circ(self.x+20,self.y-41,20,3)
        pyxel.rect(self.x,self.y-80,20,40,3)
        pyxel.circ(self.x+779,self.y-80,20,3)
        pyxel.circ(self.x+779,self.y-41,20,3)
        pyxel.rect(self.x+780,self.y-80,20,40,3)
        pyxel.rect(self.x + 20, self.y - 85, 760, 50, 5)
        #l'argent
        self.show_money()
        
    def show_money(self):
        #affiche l'argent
        self.font.text(self.x + 50, self.y - 70, f"Argent: {self.CHAT.money}")
        #affiche la mise
        self.font.text(self.x + 500, self.y - 70, f"Mise: {self.mise}")

    def machine(self):
        #le rectangle du milieu
        pyxel.rect(self.x + 50, self.y, 700, 400, 3)
        pyxel.rect(self.x, self.y + 50, 50, 300, 3)
        pyxel.rect(self.x + 750, self.y + 50, 50, 300, 3)
        pyxel.circ(self.x + 50, self.y + 50, 50, 3)
        pyxel.circ(self.x + 50, self.y + 349, 50, 3)
        pyxel.circ(self.x + 749, self.y + 50, 50, 3)
        pyxel.circ(self.x + 749, self.y + 349, 50, 3)
        #le levier
        pyxel.rect(self.x + 799, self.y + 299, 20, 10, 7)
        pyxel.rect(self.x + 819, self.y + 294, 20, 20, 7)
        pyxel.rect(self.x + 824, self.y + 144, 10, 150, 7)
        pyxel.circ(self.x + 829, self.y + 124, 20, 8) #la boule rouge
        
        self.draw_empty_cases()
        
    def draw_empty_cases(self):
        #les cases qui host les images
        for k in range(3):
            pyxel.rect(self.x + 80 + k * 220, self.y + 100, 200, 200, 1)
        
            
      
    def display_results(self):
        #affiche les cases des résultats
        for i in range(3):
            if self.results_name[i] != "":
                pyxel.image(0).load(0, 0, f"assets/Machine_sous/{self.results_name[i]}.png")
                pyxel.blt(self.x+80 + 220 * i, self.y+100, 0, 0, 0, 200, 200)

    def money_taker(self):
        #contour de l'encoche
        pyxel.rect(self.x+180,self.y+450,440,101,3)
        pyxel.rect(self.x+160,self.y+470, 20,60,3)
        pyxel.rect(self.x + 620, self.y + 470, 20, 60, 3)
        pyxel.tri(self.x +180,self.y+450,self.x+160,self.y+470,self.x+180,self.y+470,3)
        pyxel.tri(self.x + 160, self.y + 530, self.x + 180, self.y + 530, self.x + 180, self.y + 550, 3)
        pyxel.tri(self.x + 639, self.y + 470, self.x + 619, self.y + 470, self.x + 619, self.y + 450, 3)
        pyxel.tri(self.x + 639, self.y + 530, self.x + 619, self.y + 530, self.x + 619, self.y + 550, 3)
        
        #encoche
        pyxel.rect(self.x + 200, self.y + 480, 400, 35, 0)
        
    def play(self):
        self.reset_game()
        self.set_randoms()
        self.update_results()
        
    def reset_game(self):
        for k in range(3):
            self.results_name[k] = ""
        self.can_play = False
        self.frames_counter = -1
        
    def set_randoms(self):
        #les résultat de la machine
        for k in range(3):
            self.results_number[k] = randint(1, 100)
            print(self.results_number)
            
            
    def update_results(self):
        #affiche les images des cases
        for k in range(3):
            if self.results_number[k] <= 50:
                self.results_name[k] = "chat7"
            elif 50<self.results_number[k] <= 75:
                self.results_name[k] = "chat_citron_casque"
            elif 75<self.results_number[k]<= 95:
                self.results_name[k] = "chat_orange"
            else:
                self.results_name[k] = "chat_bar"
        
    def money_won(self):
        first = self.results_name[0]
        second = self.results_name[1]
        third = self.results_name[2]
        
        gain = {"chat7": self.proba_chat7, "chat_citron_casque": self.proba_chat_citron_casque, "chat_orange": self.proba_chat_orange, "chat_bar": self.proba_chat_bar}
        #le joueur n'a rien gagné
        if (first != second) and (first != third) and (second != third):
            print("no_win")
            return 0
        
        print(first, second, third, self.results_name)        
        if first == second == third:
            print("win triple", third)
            return round(self.mise / gain[first] ** 2)
        
        if (first == second) or (first == third) or (second == third):
            #trouve le résultat qui est en double
            result = {first: 0, second: 0, third: 0}
            print(result)
            for k in range(3):
                if self.results_name[k] in result.keys():
                    result[self.results_name[k]] += 1
            print(result)
            
            doublon = self.find_duplicate(result)
            
            print("win double", doublon)
            print(round(self.mise / math.sqrt(gain[doublon])))
            return round(self.mise / math.sqrt(gain[doublon]))
        
    def find_duplicate(self, result):
        for key, value in result.items():
                if value == 2:
                    print(key)
                    return key
        
    def update_money(self):
        print("update money")
        self.CHAT.money += self.money_won()
        #peut lander le prochain tirage
        self.frames_counter = 0
        self.can_play = True
        self.mise = 0
            
            
            
            
            
            