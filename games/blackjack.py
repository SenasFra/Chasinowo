import pyxel
from assets.font.PyxelUnicode import PyxelUnicode
from assets.tokens.tokens_opti.token_1 import Token_1
from assets.tokens.tokens_opti.token_2 import Token_2
from assets.tokens.tokens_opti.token_5 import Token_5
from assets.tokens.tokens_opti.token_10 import Token_10
from assets.tokens.tokens_opti.token_20 import Token_20
from assets.tokens.tokens_opti.token_50 import Token_50
import random
import time
"""
changer la valeur de l'as: faire qu'elle fasse 1 ou 11 en fonction de la main du joueur

"""

#todo check l'affichage des cartes

class Blackjack():
    def __init__(self, CHAT):

        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.font_hand_value = PyxelUnicode("assets/font/pixelmix.ttf", 30)
        self.font_token_value = PyxelUnicode("assets/font/pixelmix.ttf", 12)
        self.range_x = [410, 630]
        self.range_y = [355, 435]
        self.jouer = True
        self.CHAT = CHAT
        self.mise = 0
        
        #les jetons
        self.token_1 = Token_1()
        self.token_2 = Token_2()
        self.token_5 = Token_5()
        self.token_10 = Token_10()
        self.token_20 = Token_20()
        self.token_50 = Token_50()
        self.token_x = 1200
        self.token_y = 170
        self.tokens = {1: self.token_1, 2: self.token_2, 5: self.token_5, 10: self.token_10, 20: self.token_20, 50: self.token_50}
        self.token_value = {1: 100, 2: 200, 5: 500, 10: 1000, 20: 2000, 50: 5000}
        self.token_taken = 0
        self.tokens_on_board = []
        
        #positions des cases du croupier et du joueur pour les valeurs de la main
        self.dealer_value_position = {'x': 1065, 'y': 260}
        self.player_value_position = {'x': 250, 'y': 380}
        self.deck_range_position = [{'x': 90, 'y': 15}, {'x': 225, 'y': 185}]

        #Ces variables vont servir à créer le deck et initialiser la partie
        self.valeur = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        self.signe = ["coeur", "carreau", "trefle", "pique"]

        self.dealer_hand = []
        self.player_hand = []

        self.dealer_value = 0
        self.player_value = 0

        self.deck = []
        self.cards = []

        self.dealer_drawed_card = {}
        self.drawed_card = {}

        self.is_draw = False
        self.has_won = False
        self.has_lost = False
        self.game_ended = False
        self.game_started = False
        self.game_can_be_restarted = False

        self.HIT_or_STAND = ""


    def update(self):
        #quitte le jeu
        if pyxel.btnp(pyxel.KEY_A) and not self.game_started:
            #si le joueur avait misé
            if self.mise > 0:
                self.CHAT.money += self.mise
            self.jouer = False
            
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x
            y = pyxel.mouse_y
            print(self.CHAT.money, self.HIT_or_STAND, pyxel.mouse_x, pyxel.mouse_y)
            print(self.game_started, self.game_ended)
                
            if not self.game_started:
                #prend un jeton
                if self.token_x <= x <= self.token_x + 40 and self.token_y <= y <= self.token_y + 50 * 6:
                    self.takeToken(y)
                #ajoute le jeton pris dans la liste des jetons du rectangle entre les 2 boutons
                self.place_token_in_game(x, y)
            
            #clique sur l'un des bouton HIT STAND
            if self.game_started:
                self.chose_HIT_or_STAND()
            
            #lance la partie si on clique sur le paquet de carte
            self.has_clicked_on_deck = self.deck_range_position[0]['x'] <= x <= self.deck_range_position[1]['x'] and self.deck_range_position[0]['y'] <= y <= self.deck_range_position[1]['y']
            if not self.game_started and self.has_clicked_on_deck and self.mise > 0:
                self.start_game()
                self.init_game()
                
    def draw(self):
        pyxel.mouse(True)
        #affichage de tout ce qu'il y a sur le plateau
        self.generate_board()
        self.Maou()
        
        self.display_tokens()
        
        self.show_money()
        self.show_dealer_value()
        self.show_player_value()
        
        self.display_tokens_on_board()

        #le déroulement du jeu
        self.display_dealer_deck()
        self.display_player_deck()
            
        if self.game_started and not self.game_ended:
            #affiche les cartes du joueur
            self.play()
            self.update_money()
            if (self.game_result == "Perdu" or self.game_result == "Gagné" or self.game_result == "Egalité") and not self.game_can_be_restarted and not self.game_started:
                self.restart_game()
        
        self.cursor(pyxel.mouse_x, pyxel.mouse_y)
        
    def show_money(self):
        #affiche l'argent
        self.font.text(405, 360, f"Argent: {self.CHAT.money}")
        #affiche la mise
        self.font.text(800, 360, f"Mise: {self.mise}")
        
    def cursor(self, x, y):
        if self.token_taken != 0:
            self.tokens[self.token_taken].dess(x - 15, y - 15)
        
    def display_tokens(self):
        k = 0
        #parcours la liste des jetons et appelle la fonction qui permet de les afficher
        for n, token in self.tokens.items():
            token.dess(self.token_x,  self.token_y + 50 * k)
            self.font_token_value.text(self.token_x + 40 + 10, self.token_y + 15 + (40 * 1.25) * k, str(self.token_value[n]))
            k+=1
            
    def display_tokens_on_board(self):
        if len(self.tokens_on_board) != 0:
            for token in self.tokens_on_board:
                token["token"].dess(token["x"] - 20, token["y"] - 20)
            
    def show_dealer_value(self):
        #affiche la valeur de la main du croupier
        if self.dealer_value != 0:
            self.font_hand_value.text(self.dealer_value_position['x'], self.dealer_value_position['y'], str(self.dealer_value))
            
    def show_player_value(self):
        #affiche la valeur de la main du joueur
        if self.player_value != 0:
            self.font_hand_value.text(self.player_value_position['x'], self.player_value_position['y'], str(self.player_value))
            
    def display_dealer_deck(self):
        if len(self.dealer_hand) != 0:
            for n, dealer_card in enumerate(self.dealer_hand):
                if dealer_card.get("faced_down"):
                    pyxel.image(0).load(0, 0, f"assets/PNG-cards-1.3/back.png")
                    pyxel.blt(700 - 75 * len(self.dealer_hand) + 150 * n, 115, 0, 0, 0, 103, 150)
                else:
                    pyxel.image(0).load(0, 0, f"assets/PNG-cards-1.3/{str(dealer_card['valeur'])}_{dealer_card['signe']}.png")
                    pyxel.blt(700 - 75 * len(self.dealer_hand) + 150 * n, 115, 0, 0, 0, 103, 150)
                
    def display_player_deck(self):
        if len(self.player_hand) != 0:
            for n, player_card in enumerate(self.player_hand):
                pyxel.image(0).load(0, 0, f"assets/PNG-cards-1.3/{str(player_card['valeur'])}_{player_card['signe']}.png")
                pyxel.blt(700 - 75 * len(self.player_hand) + 150 * n, 405, 0, 0, 0, 103, 150)


    def generate_board(self):
        #charge le plateau
        for x in range(6):
            for y in range(0, 4):
                pyxel.image(0).load(0, 0, f"assets/blackjack/{x}{y}.png")
                pyxel.blt(x * 225, y * 170, 0, 0, 0, 225, 170)

    def takeToken(self, y):
        #change la valeur du jeton qui a été pris
        size = 40
        gap = 10
        #jeton 1
        if self.token_y <= y <= self.token_y + size and self.CHAT.money >= 100:
            self.token_taken = 1
        #jeton 2
        elif self.token_y + (size + gap) <= y <= self.token_y + 2 * size + gap and self.CHAT.money >= 200:
            self.token_taken = 2
        #jeton 5
        elif self.token_y + 2 * (size + gap) <= y <= self.token_y + 3 * size + 2 * gap and self.CHAT.money >= 500:
            self.token_taken = 5
        #jeton 10
        elif self.token_y + 3 * (size + gap) <= y <= self.token_y + 4 * size + 3 * gap and self.CHAT.money >= 1000:
            self.token_taken = 10
        #jeton 20
        elif self.token_y + 4 * (size + gap) <= y <= self.token_y + 5 * size + 4 * gap and self.CHAT.money >= 2000:
            self.token_taken = 20
        #jeton 50
        elif self.token_y + 5 * (size + gap) <= y <= self.token_y + 6 * size + 5 *gap and self.CHAT.money >= 5000:
            self.token_taken = 50
        else:
            self.token_taken = 0
            
    def place_token_in_game(self, x, y):
        #on a un jeton dans la main
        if self.token_taken != 0:
            #ajoute le jeton à la liste des jetons posés sur le plateau
            if 535 + 20 <= x <= 810 - 20 and 570 + 20 <= y <= 660 - 20:
                self.tokens_on_board.append({"token": self.tokens[self.token_taken], "x": x, "y": y})
                #augmente la mise selon le jeton posé
                self.mise += self.token_value[self.token_taken]
                self.CHAT.money -= self.token_value[self.token_taken]
                self.token_taken = 0 #réinitialise le jeton
                
    def create_deck(self):
        #crée le jeu de cartes
        for i in range(len(self.valeur)):
            for k in range(len(self.signe)):
                self.deck.append({"valeur": self.valeur[i], "signe": self.signe[k]})

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def create_dealer_hand(self):
        #donne 2 cartes au croupier
        for k in range(2):
            if k == 1:
                self.deck[-1]["faced_down"] = True
            self.dealer_hand.append(self.deck[-1])
            self.deck.pop()

    def create_player_hand(self):
        #donne 2 cartes au joueur
        for k in range(2):
            self.player_hand.append(self.deck[-1])
            self.deck.pop()

    def get_value_from_card(self, card, player_or_dealer):
        #si la valeur de la carte est un nombre, on renvoie directement ce nombre
        if type(card["valeur"]) is int:
            return card["valeur"]
        
        #la carte est un As
        if card["valeur"] == "A":
            #le croupier a plus de 21 avec l'As à 11 ou si le joueur a plus de 21 avec l'As à 11
            print(player_or_dealer, self.dealer_value, self.player_value)
            if (player_or_dealer == "dealer" and self.dealer_value + 11 > 21) or (player_or_dealer == "player" and self.player_value + 11 > 21):
                return 1
            #sinon l'As vaut 11
            return 11
        
        #la carte est un valet, une dame ou un roi
        return 10
        
    def get_dealer_value(self):
        #la valeur du croupier est la 1ère carte si la 2e est retournée
        total = 0
        for dealer_card in self.dealer_hand:
            if not dealer_card.get("faced_down"):
                total += self.get_value_from_card(dealer_card, "dealer")
        return total

    def dealer_draw(self):
        #fais piocher le croupier
        self.dealer_hand.append(self.deck[-1])
        self.dealer_drawed_card = self.deck[-1]
        self.deck.pop()

    def player_draw(self):
        #fais piocher le joueur
        self.player_hand.append(self.deck[-1])
        self.drawed_card = self.deck[-1]
        self.deck.pop()
        

    def end_game(self):
        #si le joueur a la même valeur que le croupier et que l'on a pas encore pioché
        if self.player_value == self.dealer_value and self.dealer_value >= 17:
            self.is_draw = True
            self.game_ended = True
            self.game_started = False
            return "Egalité"
        
        """Le joueur gagne"""
        #si le joueur a plus que le croupier et que le croupier a plus de 17
        if self.player_value > self.dealer_value and self.dealer_value >= 17 and self.player_value < 21:
            self.has_won = True
            self.game_ended = True
            self.game_started = False
            return "Gagné"
        #si le joueur a blackjack (avoir 21)
        if self.player_value == 21:
            self.has_won = True
            self.game_ended = True
            self.game_started = False
            return "Gagné"
        #si le croupier dépasse 21
        if self.dealer_value > 21:
            self.has_won = True
            self.game_ended = True
            self.game_started = False
            return "Gagné"
        
        """Le joueur perd"""
        #si le croupier a blackjack (avoir 21)
        if self.dealer_value == 21:
            self.has_lost = True
            self.game_ended = True
            self.game_started = False
            return "Perdu"
        #si le joueur dépasse 21
        if self.player_value > 21:
            self.has_lost = True
            self.game_ended = True
            self.game_started = False
            return "Perdu"
        #si le croupier a 17 ou plus et a plus que le joueur
        if self.dealer_value >= 17 and self.dealer_value > self.player_value:
            self.has_lost = True
            self.game_ended = True
            self.game_started = False
            return "Perdu"
        
    def update_money(self):
        if self.has_won:
            self.CHAT.money += 2 * self.mise
        elif self.is_draw:
            self.CHAT.money += self.mise

    def new_player_value(self, card):
        #change la valeur de la main du joueur après qu'il ait pioché
        new_player_value = self.player_value + self.get_value_from_card(card, "player")
        return new_player_value

    def new_dealer_value(self, card):
        #change la valeur de la main du croupier après qu'il ait pioché
        new_dealer_value = self.dealer_value + self.get_value_from_card(card, "dealer")
        return new_dealer_value
    
    def start_game(self):
        #active la variable qui lance la partie si on clique sur le deck et qu'on a une mise
        self.game_started = True
            
        if self.game_can_be_restarted:
            self.dealer_hand = []
            self.player_hand = []

            self.dealer_value = 0
            self.player_value = 0

            self.deck = []
            self.cards = []

            self.dealer_drawed_card = {}
            self.drawed_card = {}

            self.is_draw = False
            self.has_won = False
            self.has_lost = False
            self.game_ended = False
            self.game_can_be_restarted = False

            self.HIT_or_STAND = ""
        
    def chose_HIT_or_STAND(self):
        #clique sur le bouton HIT
        if 300 <= pyxel.mouse_x <= 500 and 584 <= pyxel.mouse_y <= 654:
            self.HIT_or_STAND = "HIT"
        #clique le sur le bouton STAND
        if 850 <= pyxel.mouse_x <= 1050 and 584 <= pyxel.mouse_y <= 654:
            self.HIT_or_STAND = "STAND"
            
    def init_game(self):
        #initialise la partie
        self.create_deck()
        self.shuffle_deck()
        self.create_player_hand()
        self.create_dealer_hand()

        self.dealer_value = self.get_dealer_value()
        self.player_value = self.get_value_from_card(self.player_hand[0], "player")
        self.player_value += self.get_value_from_card(self.player_hand[1], "player")
        
        
    def play(self):
        #le déroulement du jeu
        self.game_result = self.end_game()
        if self.game_result is not None:
            print(self.game_result, self.player_value)
            
        if self.game_result != "Perdu" and self.game_result != "Gagné" and self.game_result != "Egalité":
                
            if self.HIT_or_STAND == "HIT":
                #le joueur pioche
                self.player_draw()
                self.player_value = self.new_player_value(self.drawed_card)
                self.HIT_or_STAND = ""
            elif self.HIT_or_STAND == "STAND":
                #le croupier retourne sa carte
                self.dealer_hand[1]["faced_down"] = False
                self.dealer_value = self.get_dealer_value()
                #le joueur attend que le croupier termine de piocher
                while self.dealer_value < 17:
                    self.dealer_draw()
                    self.dealer_value = self.new_dealer_value(self.dealer_drawed_card)
                    
        

                    
    def restart_game(self):
        self.mise = 0
        self.tokens_on_board = []
        
        self.game_ended = False
        self.game_can_be_restarted = True
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def Maou(self):
        pyxel.rect(390, 15, 560, 75, 5)

