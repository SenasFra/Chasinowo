import pyxel

from random import randint

class Roulette():
    def __init__(self, user_money):
        self.user_money = user_money
        self.wages = []
        self.bets = []
        self.result = 0
        
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

        self.token_gap = 50
        self.x_1_token = 80
        self.x_2_token = self.x_1_token + self.token_gap
        self.x_5_token = self.x_2_token + self.token_gap
        self.x_10_token = self.x_5_token + self.token_gap
        self.x_20_token = self.x_10_token + self.token_gap
        self.x_50_token = self.x_20_token + self.token_gap

        self.y_token = 500

        self.token_radius = 20

        self.token_taken = 0
        self.token_color = {1: 14, 2: 10, 5: 11, 10: 12, 20: 13, 50: 0}
        self.token_value = {1: 10000, 2: 20000, 5: 50000, 10: 100000, 20: 200000, 50: 500000}

        self.tokens_on_board = []

        self.coord = []
        
        #les couleurs
        self.red_numbers  = [1, 3,  5, 7, 9, 12,  14,  16, 18, 19, 21, 23, 25, 27, 30, 32, 36]
        self.black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 34, 35]

        
        pyxel.init(1350, 670)
        pyxel.cls(1)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            
            #prend un jeton
            if self.x_1_token - self.token_radius < x < self.x_50_token + self.token_radius and  self.y_token - self.token_radius < y < self.y_token + self.token_radius:
                self.takeToken(x)
                
            #lance la roulette:
            if len(self.tokens_on_board) != 0 and (50 < x < self.x_0_column and self.y_1_line < y < self.y_6_line):
                self.play()

                
            self.placeTokenOnBoard(x, y)
            print(self.user_money, self.result)
            
            print(self.bets, self.wages)
                
    def draw(self):
        pyxel.cls(1)
        
        for x in range(6):
            for y in range(1, 4):
                pyxel.image(0).load(0,0, f"./Images/roulette_img/{x}{y}.jpg")
                pyxel.blt(x * 225,  (y - 1) * 150, 0, 0, 0, 225, 150)
                
        
        #les jetons
        self.draw7Tokens()
        
        #crée le curseur
        self.cursor(pyxel.mouse_x, pyxel.mouse_y)
        
        #affiche les jetons posés sur le plateau
        if len(self.tokens_on_board) != 0:
            for token in self.tokens_on_board:
                pyxel.circ(token['x'], token['y'], token['radius'], token['color'])

    def roulette_results(self):
        for i in range(len(self.bets)):
            print(self.user_money, self.result, self.bets[i], self.wages[i])           
            bet = self.bets[i]
            wage = self.wages[i]
            
            double_the_wage = (bet == "1 to 18" and self.result in range(1, 19)) or (bet == "19 to 36" and self.result in range(19, 36)) \
                or (type(bet) is int and (bet == "even" and self.result % 2 == 0) or (bet == "odd" and self.result % 2 != 0)) \
                or (bet == "red" and self.result in self.red_numbers) or (bet == "black" and self.result in self.black_numbers)

            triple_the_wage = (bet == "first 12" and self.result in range(1, 13)) or (bet == "second 12" and self.result in range(13, 25))  or (bet == "third 12" and self.result in range(25, 37)) \
                or (bet == "first 2 to 1" and self.result in range(1, 13)) or (bet == "second 2 to 1" and self.result in range(13, 25))  or (bet == "third 2 to 1" and self.result in range(25, 37))
            
            if double_the_wage:
                self.user_money += wage * 2
            elif triple_the_wage:
                self.user_money += wage * 3
            elif type(bet) is int and bet == self.result:
                self.user_money += wage * 36
            else:
                self.user_money += 0
            
            
            
    def play(self):
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
        
        #les résultats de la roulette
        self.result = randint(0,36)       
        self.roulette_results()
        
        self.resetGame()
            
    def resetGame(self):
        #il y a autant de mises que de jetons sur le tebleau 
        while len(self.tokens_on_board) != 0:
            self.tokens_on_board.pop()
            self.bets.pop()
            self.wages.pop()

        
    def placeToken(self, x, y):
        self.tokens_on_board.append({'x': x // 2, 'y': y // 2, 'radius': self.token_radius, 'color': self.token_color[self.token_taken]}) #pose le jeton sur le plateau
        self.wages.append(self.token_value[self.token_taken])
        self.user_money -= self.token_value[self.token_taken]
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
            

    def draw7Tokens(self):
        pyxel.circ(self.x_1_token, self.y_token, self.token_radius, self.token_color[1])
        pyxel.circ(self.x_2_token, self.y_token, self.token_radius, self.token_color[2])
        pyxel.circ(self.x_5_token, self.y_token, self.token_radius, self.token_color[5])
        pyxel.circ(self.x_10_token, self.y_token, self.token_radius, self.token_color[10])
        pyxel.circ(self.x_20_token, self.y_token, self.token_radius, self.token_color[20])
        pyxel.circ(self.x_50_token, self.y_token, self.token_radius, self.token_color[50])
        
        
    def takeToken(self, x):
        #jeton 1
        if self.x_1_token - self.token_radius < x < self.x_1_token + self.token_radius and self.user_money >= 10000:
            self.token_taken = 1
        #jeton 2
        elif self.x_2_token - self.token_radius < x < self.x_2_token + self.token_radius and self.user_money >= 20000:
            self.token_taken = 2
        #jeton 5
        elif self.x_5_token - self.token_radius < x < self.x_5_token + self.token_radius and self.user_money >= 50000:
            self.token_taken = 5
        #jeton 10
        elif self.x_10_token - self.token_radius < x < self.x_10_token + self.token_radius and self.user_money >= 100000:
            self.token_taken = 10
        #jeton 20
        elif self.x_20_token - self.token_radius < x < self.x_20_token + self.token_radius and self.user_money >= 200000:
            self.token_taken = 20
        #jeton 50
        elif self.x_50_token - self.token_radius < x < self.x_50_token + self.token_radius and self.user_money >= 500000:
            self.token_taken = 50
        else:
            self.token_taken = 0

            

    def cursor(self, x, y):
        if self.token_taken != 0:
            pyxel.circ(x, y, self.token_radius, self.token_color[self.token_taken])
        else: 
            pyxel.circ(x, y, 8, 7)
            
        


    



Roulette(50000)