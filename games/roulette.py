import pyxel
from assets.font.PyxelUnicode import PyxelUnicode

from random import randint
from assets.tokens.tokens_opti.token_1 import Token_1
from assets.tokens.tokens_opti.token_2 import Token_2
from assets.tokens.tokens_opti.token_5 import Token_5
from assets.tokens.tokens_opti.token_10 import Token_10
from assets.tokens.tokens_opti.token_20 import Token_20
from assets.tokens.tokens_opti.token_50 import Token_50

class Roulette():
    def __init__(self, CHAT):
        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.font_token_value = PyxelUnicode("assets/font/pixelmix.ttf", 12)
        self.range_x = [405, 465]
        self.range_y = [265, 350]
        self.jouer = True
        self.CHAT = CHAT
        
        self.wages = []
        self.bets = []
        self.result = -1
        
        #coordonnées des lignes du plateau
        self.y_1_line = 30
        self.y_2_line = 110
        self.y_3_line = 190
        self.y_4_line = 270
        self.y_5_line = 340
        self.y_6_line = 400

        self.x_0_column = 470
        self.x_1_column = 565
        self.x_2_column = 620
        self.x_3_column = 680
        self.x_4_column = 735
        self.x_5_column = 790
        self.x_6_column = 850
        self.x_7_column = 905
        self.x_8_column = 960
        self.x_9_column = 1020
        self.x_10_column = 1075
        self.x_11_column = 1130
        self.x_12_column = 1190
        self.x_13_column = 1245
        self.x_14_column = 1300

        #attributs des jetons
        self.token_diameter = 40
        self.token_gap = self.token_diameter + 10
        self.x_1_token = 80
        self.x_2_token = self.x_1_token + self.token_gap
        self.x_5_token = self.x_2_token + self.token_gap
        self.x_10_token = self.x_5_token + self.token_gap
        self.x_20_token = self.x_10_token + self.token_gap
        self.x_50_token = self.x_20_token + self.token_gap

        self.y_token = 500
        
        self.token_1 = Token_1()
        self.token_2 = Token_2()
        self.token_5 = Token_5()
        self.token_10 = Token_10()
        self.token_20 = Token_20()
        self.token_50 = Token_50()

        self.token_taken = 0
        self.tokens = {1: self.token_1, 2: self.token_2, 5: self.token_5, 10: self.token_10, 20: self.token_20, 50: self.token_50}
        self.token_color = {1: 14, 2: 10, 5: 11, 10: 12, 20: 13, 50: 0}
        self.token_value = {1: 10000, 2: 20000, 5: 50000, 10: 100000, 20: 200000, 50: 500000}

        self.tokens_on_board = []
        
        #les couleurs
        self.red_numbers  = [1, 3,  5, 7, 9, 12,  14,  16, 18, 19, 21, 23, 25, 27, 30, 32, 36]
        self.black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 34, 35]
        
    def update(self):
        #quitte le jeu 
        
        
        if pyxel.btnp(pyxel.KEY_A):
            self.jouer = False
            
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            print(x, y)
            #prend un jeton
            if self.x_1_token < x < self.x_50_token + self.token_diameter and  self.y_token < y < self.y_token + self.token_diameter:
                self.takeToken(x)
                
            #lance la roulette:
            if len(self.tokens_on_board) != 0 and (50 < x < self.x_0_column and self.y_1_line < y < self.y_6_line):
                self.play()

            self.placeTokenOnBoard(x, y)
                
    def draw(self):
        pyxel.cls(1)
        
        #affiche le plateau
        for x in range(6):
            for y in range(1, 4):
                pyxel.image(0).load(0,0, f"assets/roulette/{x}{y}.jpg")
                pyxel.blt(x * 225,  (y - 1) * 150, 0, 0, 0, 225, 150)
                
        
        #les jetons que l'on peut choisir
        self.draw6Tokens()
        
        #les jetons posés sur le plateau
        self.displayTokensOnBoard()
        
        #crée le curseur
        self.cursor(pyxel.mouse_x, pyxel.mouse_y)
        
        
                
        #affiche le résultat, l'argent du joueur
        if self.result != -1:
            self.font.text(850, 500, f"Resultat: {self.result}")
            self.add_ball_on_roulette()
        self.font.text(500, 500, f"Argent : {self.CHAT.money}")

    def play(self):
        #les résultats de la roulette
        self.result = randint(0,36)       
        self.roulette_results()
        self.resetGame()
        
    def add_ball_on_roulette(self):
            coordRouletteBall = {0: [317, 120], 1: [137, 244], 2: [369, 223], 3: [280, 104], 4: [362, 181], 5: [179, 309], 6: [340, 293], 7: [201, 113], 8: [232, 331], 9: [145, 164], 10: [196, 319], 11: [271, 332],
            12: [241, 99], 13: [308, 319], 14: [133, 203], 15: [345, 148], 16: [150, 279], 17: [361, 261], 18: [168, 133], 19: [357, 164], 20: [134, 223], 21: [371, 203], 22: [159, 149], 23: [211, 327], 24: [163, 294],
            25: [368, 243], 26: [299, 109], 27: [326, 311], 28: [221, 106], 29: [187, 121], 30: [251, 335], 31: [140, 184], 32: [333, 132], 33: [142, 260], 34: [351, 276], 35: [261, 102], 36: [289, 327]}
        
            x, y = coordRouletteBall[self.result][0], coordRouletteBall[self.result][1]
            pyxel.circ(x, y, 5, 7)
        
        
    def roulette_results(self):
        for i in range(len(self.bets)):
            print(self.CHAT.money, self.result, self.bets[i], self.wages[i])           
            bet = self.bets[i]
            wage = self.wages[i]
            
            #règles simplifiées
            """
            on peut parier sur:
            -1 to 18
            -even
            -red
            -black
            -odd
            -19 to 36
            => X2
            -1st 12
            -2nd 12
            -3rd 12
            => X3
            -number
            => X36
            """
            double_the_wage = (bet == "1 to 18" and self.result in range(1, 19)) or (bet == "19 to 36" and self.result in range(19, 36)) \
                or ((bet == "even" and self.result % 2 == 0) or (bet == "odd" and self.result % 2 != 0)) \
                or (bet == "red" and self.result in self.red_numbers) or (bet == "black" and self.result in self.black_numbers)

            triple_the_wage = (bet == "first 12" and self.result in range(1, 13)) or (bet == "second 12" and self.result in range(13, 25))  or (bet == "third 12" and self.result in range(25, 37)) \
                or (bet == "first 2 to 1" and self.result in range(1, 13)) or (bet == "second 2 to 1" and self.result in range(13, 25))  or (bet == "third 2 to 1" and self.result in range(25, 37))
            
            if double_the_wage:
                self.CHAT.money += wage * 2
            elif triple_the_wage:
                self.CHAT.money += wage * 3
            elif type(bet) is int and bet == self.result:
                self.CHAT.money += wage * 36
            else:
                self.CHAT.money += 0
            
            
            
            
    def resetGame(self):
        #retire les jetons du plateau
        while len(self.tokens_on_board) != 0:
            self.tokens_on_board.pop()
        #réinitialise les paris
        while len(self.bets) != 0:
            self.bets.pop()
        while len(self.wages) != 0:
            self.wages.pop()
            
    def displayTokensOnBoard(self):
        #affiche les jetons posés sur le plateau
        if len(self.tokens_on_board) != 0:
            for token in self.tokens_on_board:
                # pyxel.image(0).load(0,0, f"assets/tokens/token_{token['color']}.png")
                # pyxel.blt(token['x'],  token['y'], 0, 0, 0, 40, 40)
                token["token"].dess(token['x'], token['y'])

        
    def placeToken(self, x, y):
        #self.tokens_on_board.append({'x': x // 2 - 20, 'y': y // 2 - 20, 'diameter': self.token_diameter, 'color': self.token_taken}) #pose le jeton sur le plateau
        self.tokens_on_board.append({"token": self.tokens[self.token_taken], 'x': x // 2 - 20, 'y': y // 2 - 20}) #pose le jeton sur le plateau
        
        self.wages.append(self.token_value[self.token_taken])
        self.CHAT.money -= self.token_value[self.token_taken]
        self.token_taken = 0
                
    def placeTokenOnBoard(self, x, y):
        if self.token_taken != 0: 
            #case 0
            if self.x_0_column < x < self.x_1_column and self.y_1_line < y < self.y_4_line:
                self.placeToken(self.x_0_column + self.x_1_column, self.y_1_line + self.y_4_line)
                self.bets.append(0)
            #case 1
            elif self.x_1_column <= x <= self.x_2_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_1_column + self.x_2_column, self.y_3_line + self.y_4_line)
                self.bets.append(1)
            #case 2
            elif self.x_1_column <= x <= self.x_2_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_1_column + self.x_2_column, self.y_2_line + self.y_3_line)
                self.bets.append(2)
            #case 3
            elif self.x_1_column <= x <= self.x_2_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_1_column + self.x_2_column, self.y_1_line + self.y_2_line)
                self.bets.append(3)
            #case 4
            elif self.x_2_column <= x <= self.x_3_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_2_column + self.x_3_column, self.y_3_line + self.y_4_line)
                self.bets.append(4)
            #case 5
            elif self.x_2_column <= x <= self.x_3_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_2_column + self.x_3_column, self.y_2_line + self.y_3_line)
                self.bets.append(5)
            #case 6
            elif self.x_2_column <= x <= self.x_3_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_2_column + self.x_3_column, self.y_1_line + self.y_2_line)
                self.bets.append(6)
            #case 7
            elif self.x_3_column <= x <= self.x_4_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_3_column + self.x_4_column, self.y_3_line + self.y_4_line)
                self.bets.append(7)
            #case 8
            elif self.x_3_column <= x <= self.x_4_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_3_column + self.x_4_column, self.y_2_line  + self.y_3_line)
                self.bets.append(8)
            #case 9
            elif self.x_3_column <= x <= self.x_4_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_3_column + self.x_4_column, self.y_1_line + self.y_2_line)
                self.bets.append(9)
            #case 10
            elif self.x_4_column <= x <= self.x_5_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_4_column + self.x_5_column, self.y_3_line + self.y_4_line)
                self.bets.append(10)
            #case 11
            elif self.x_4_column <= x <= self.x_5_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_4_column + self.x_5_column, self.y_2_line + self.y_3_line)
                self.bets.append(11)
            #case 12
            elif self.x_4_column <= x <= self.x_5_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_4_column + self.x_5_column, self.y_1_line + self.y_2_line)
                self.bets.append(12)
            #case 13
            elif self.x_5_column <= x <= self.x_6_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_5_column + self.x_6_column, self.y_3_line + self.y_4_line)
                self.bets.append(13)
            #case 14
            elif self.x_5_column <= x <= self.x_6_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_5_column + self.x_6_column, self.y_2_line + self.y_3_line)
                self.bets.append(14)
            #case 15
            elif self.x_5_column <= x <= self.x_6_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_5_column + self.x_6_column, self.y_1_line + self.y_2_line)
                self.bets.append(15)
            #case 16
            elif self.x_6_column <= x <= self.x_7_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_6_column + self.x_7_column, self.y_3_line + self.y_4_line)
                self.bets.append(16)
            #case 17
            elif self.x_6_column <= x <= self.x_7_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_6_column + self.x_7_column, self.y_2_line + self.y_3_line)
                self.bets.append(17)
            #case 18
            elif self.x_6_column <= x <= self.x_7_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_6_column + self.x_7_column, self.y_1_line + self.y_2_line)
                self.bets.append(18)
            #case 19
            elif self.x_7_column <= x <= self.x_8_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_7_column + self.x_8_column, self.y_3_line + self.y_4_line)
                self.bets.append(19)
            #case 20
            elif self.x_7_column <= x <= self.x_8_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_7_column + self.x_8_column, self.y_2_line + self.y_3_line)
                self.bets.append(20)
            #case 21
            elif self.x_7_column <= x <= self.x_8_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_7_column + self.x_8_column, self.y_1_line + self.y_2_line)
                self.bets.append(21)
           #case 22
            elif self.x_8_column <= x <= self.x_9_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_8_column + self.x_9_column, self.y_3_line + self.y_4_line)
                self.bets.append(22)
            #case 23
            elif self.x_8_column <= x <= self.x_9_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_8_column + self.x_9_column, self.y_2_line + self.y_3_line)
                self.bets.append(23)
            #case 24
            elif self.x_8_column <= x <= self.x_9_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_8_column + self.x_9_column, self.y_1_line + self.y_2_line)
                self.bets.append(24)
            #case 25
            elif self.x_9_column <= x <= self.x_10_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_9_column + self.x_10_column, self.y_3_line + self.y_4_line)
                self.bets.append(25)
            #case 26
            elif self.x_9_column <= x <= self.x_10_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_9_column + self.x_10_column, self.y_2_line + self.y_3_line)
                self.bets.append(26)
            #case 27
            elif self.x_9_column <= x <= self.x_10_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_9_column + self.x_10_column, self.y_1_line + self.y_2_line)
                self.bets.append(27)
            #case 28
            elif self.x_10_column <= x <= self.x_11_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_10_column + self.x_11_column, self.y_3_line + self.y_4_line)
                self.bets.append(28)
            #case 29
            elif self.x_10_column <= x <= self.x_11_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_10_column + self.x_11_column, self.y_2_line + self.y_3_line)
                self.bets.append(29)
            #case 30
            elif self.x_10_column <= x <= self.x_11_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_10_column + self.x_11_column, self.y_1_line + self.y_2_line)
                self.bets.append(30)
            #case 31
            elif self.x_11_column <= x <= self.x_12_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_11_column + self.x_12_column, self.y_3_line + self.y_4_line)
                self.bets.append(31)
            #case 32
            elif self.x_11_column <= x <= self.x_12_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_11_column + self.x_12_column, self.y_2_line + self.y_3_line)
                #self.bets.append(32
            #case 33
            elif self.x_11_column <= x <= self.x_12_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_11_column + self.x_12_column, self.y_1_line + self.y_2_line)
                self.bets.append(33)
            #case 34
            elif self.x_12_column <= x <= self.x_13_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_12_column + self.x_13_column, self.y_3_line + self.y_4_line)
                self.bets.append(34)
            #case 35
            elif self.x_12_column <= x <= self.x_13_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_12_column + self.x_13_column, self.y_2_line + self.y_3_line)
                self.bets.append(35)
            #case 36
            elif self.x_12_column <= x <= self.x_13_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_12_column + self.x_13_column, self.y_1_line + self.y_2_line)
                self.bets.append(36)
            #case first 2 to 1
            elif self.x_13_column <= x <= self.x_14_column and self.y_1_line <= y <= self.y_2_line:
                self.placeToken(self.x_13_column + self.x_14_column, self.y_1_line + self.y_2_line)
                self.bets.append("first 2 to 1")
            #case second 2 to 1
            elif self.x_13_column <= x <= self.x_14_column and self.y_2_line <= y <= self.y_3_line:
                self.placeToken(self.x_13_column + self.x_14_column, self.y_2_line + self.y_3_line)
                self.bets.append("second 2 to 1")
            #case third 2 to 1
            elif self.x_13_column <= x <= self.x_14_column and self.y_3_line <= y <= self.y_4_line:
                self.placeToken(self.x_13_column + self.x_14_column, self.y_3_line + self.y_4_line)
                self.bets.append("third 2 to 1")
            #case first 12
            elif self.x_1_column <= x <= self.x_5_column and self.y_4_line <= y <= self.y_5_line:
                self.placeToken(self.x_1_column + self.x_5_column, self.y_4_line + self.y_5_line)
                self.bets.append("first 12")
            #case second 12
            elif self.x_5_column <= x <= self.x_9_column and self.y_4_line <= y <= self.y_5_line:
                self.placeToken(self.x_5_column + self.x_9_column, self.y_4_line + self.y_5_line)
                self.bets.append("second 12")
            #case third 12
            elif self.x_9_column <= x <= self.x_13_column and self.y_4_line <= y <= self.y_5_line:
                self.placeToken(self.x_9_column + self.x_13_column, self.y_4_line + self.y_5_line)
                self.bets.append("third 12")
            #case 1 to 18
            elif self.x_1_column <= x <= self.x_3_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_1_column + self.x_3_column, self.y_5_line + self.y_6_line)
                self.bets.append("1 to 18")
            #case even
            elif self.x_3_column <= x <= self.x_5_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_3_column + self.x_5_column, self.y_5_line + self.y_6_line)
                self.bets.append("even")
            #case red
            elif self.x_5_column <= x <= self.x_7_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_5_column + self.x_7_column, self.y_5_line + self.y_6_line)
                self.bets.append("red")
            #case black
            elif self.x_7_column <= x <= self.x_9_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_7_column + self.x_9_column, self.y_5_line + self.y_6_line)
                self.bets.append("black")
            #case odd
            elif self.x_9_column <= x <= self.x_11_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_9_column + self.x_11_column, self.y_5_line + self.y_6_line)
                self.bets.append("odd")
            #case 19 to 36
            elif self.x_11_column <= x <= self.x_13_column and self.y_5_line <= y <= self.y_6_line:
                self.placeToken(self.x_11_column + self.x_13_column, self.y_5_line + self.y_6_line)
                self.bets.append("19 to 36")
            

    def draw6Tokens(self):
        k = 0
        for n, token in self.tokens.items():
            token.dess(self.x_1_token + 50 * k,  self.y_token)
            self.font_token_value.text(self.x_1_token + 15 + (self.token_diameter * 1.25) * k, self.y_token + self.token_diameter + 10, str(self.token_value[n] // 10000))
            k+=1
        # for k, n in enumerate([1, 2, 5, 10, 20, 50]):
        #     pyxel.image(0).load(0,0, f"assets/tokens/token_{n}.png")
        #     pyxel.blt(self.x_1_token + 50 * k,  self.y_token, 0, 0, 0, 40, 40)
        
        
    def takeToken(self, x):
        #jeton 1
        if self.x_1_token < x < self.x_1_token + self.token_diameter and self.CHAT.money >= 10000:
            self.token_taken = 1
        #jeton 2
        elif self.x_2_token < x < self.x_2_token + self.token_diameter and self.CHAT.money >= 20000:
            self.token_taken = 2
        #jeton 5
        elif self.x_5_token < x < self.x_5_token + self.token_diameter and self.CHAT.money >= 50000:
            self.token_taken = 5
        #jeton 10
        elif self.x_10_token < x < self.x_10_token + self.token_diameter and self.CHAT.money >= 100000:
            self.token_taken = 10
        #jeton 20
        elif self.x_20_token < x < self.x_20_token + self.token_diameter and self.CHAT.money >= 200000:
            self.token_taken = 20
        #jeton 50
        elif self.x_50_token < x < self.x_50_token + self.token_diameter and self.CHAT.money >= 500000:
            self.token_taken = 50
        else:
            self.token_taken = 0

            

    def cursor(self, x, y):
        if self.token_taken != 0:
            self.tokens[self.token_taken].dess(x - 20, y - 20)
        else: 
            pyxel.circ(x, y, 5, 7)
            