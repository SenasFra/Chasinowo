import pyxel
from assets.font.PyxelUnicode import PyxelUnicode
from assets.tokens.tokens_opti.token_1 import Token_1
from assets.tokens.tokens_opti.token_2 import Token_2
from assets.tokens.tokens_opti.token_5 import Token_5
from assets.tokens.tokens_opti.token_10 import Token_10
from assets.tokens.tokens_opti.token_20 import Token_20
from assets.tokens.tokens_opti.token_50 import Token_50
import random


class Blackjack():
    def __init__(self):

        self.font = PyxelUnicode("assets/font/pixelmix.ttf", 20)
        self.font_token_value = PyxelUnicode("assets/font/pixelmix.ttf", 12)
        self.range_x = [405, 465]
        self.range_y = [265, 350]
        self.jouer = True

        #Ces variables vont servir à créer le deck
        self.valeur = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        self.signe = ["coeur", "carreau", "trefle", "pique"]

        self.dealer_hand = []
        self.player_hand = []

        self.dealer_value = 0
        self.player_value = 0

        self.deck = []
        self.cards = []

        self.dealer_drawed_card = []
        self.drawed_card = []

        self.is_draw = False
        self.has_won = False
        self.has_lost = False
        self.game_ended = False

        self.HIT_or_STAND = ""


    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print(pyxel.mouse_x, pyxel.mouse_y)
            if 300 <= pyxel.mouse_x <= 500 and 584 <= pyxel.mouse_y <= 654:
                print("miaou")

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 850 <= pyxel.mouse_x <= 1050 and 584 <= pyxel.mouse_y <= 654:
                print("chat")
    def draw(self):
        pyxel.mouse(True)
        for x in range(6):
            for y in range(0, 4):
                pyxel.image(0).load(0, 0, f"assets/blackjack/{x}{y}.png")
                pyxel.blt(x * 225, y * 170, 0, 0, 0, 225, 170)
        pyxel.image(0).load(0, 0, f"assets/PNG-cards-1.3/8_trefle.png")
        pyxel.blt(552, 402, 0, 0, 0, 103, 150)

    def create_deck(self):
        self.deck = []
        for i in range(len(self.valeur)):
            for k in range(len(self.signe)):
                self.deck.append([self.valeur[i], self.signe[k]])
        return self.deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def create_dealer_hand(self):
        self.dealer_hand = []
        for k in range(2):
            self.dealer_hand.append(self.deck[-1])
            self.deck.pop()
        return self.dealer_hand[0], self.dealer_hand[1]

    def create_player_hand(self):
        self.player_hand = []
        for k in range(2):
            self.player_hand.append(self.deck[-1])
            self.deck.pop()
        return self.player_hand

    def get_values_from_cards(self, card):
        if type(card[0]) is int:
            return card[0]
        elif card[0] == "A":
            return 11
        else:
            return 10

    def dealer_draw(self):
        self.dealer_hand.append(self.deck[-1])
        self.dealer_drawn_card = self.deck[-1]
        self.deck.pop()

    def player_draw(self):
        self.player_hand.append(self.deck[-1])
        self.drawn_card = self.deck[-1]
        self.deck.pop()

    def end_game(self):
        if self.player_value == self.dealer_value and len(self.player_hand) == 2:
            self.is_draw = True
            self.game_ended = True
            return "Egalité"
        if self.player_value == 21:
            self.has_won = True
            self.game_ended = True
            return "Gagné"
        if self.dealer_value == 21:
            self.has_lost = True
            self.game_ended = True
            return "Perdu"
        if self.dealer_value > 21:
            self.has_won = True
            self.game_ended = True
            return "Gagné"
        if self.player_value > 21:
            self.has_lost = True
            self.game_ended = True
            return "Perdu"

    def new_player_value(self, card):
        new_player_value = self.player_value + self.get_values_from_cards(card)
        return new_player_value

    def new_dealer_value(self, card):
        new_dealer_value = self.dealer_value + self.get_values_from_cards(card)
        return new_dealer_value

    def play(self):
        self.create_deck()
        self.shuffle_deck()
        self.create_player_hand()
        self.create_dealer_hand()
        self.game_ended = False
        self.has_won = False
        self.has_lost = False
        self.dealer_value = self.get_values_from_cards(self.dealer_hand[0]) + self.get_values_from_cards(self.dealer_hand[1])
        self.player_value = self.get_values_from_cards(self.player_hand[0]) + self.get_values_from_cards(self.player_hand[1])
        print("Main du croupier : ", self.dealer_hand)
        print("Main du joueur :   ", self.player_hand)
        print("Valeur du croupier :", self.dealer_value)
        print("Valeur du joueur   :", self.player_value)
        while self.end_game() != "Perdu" and self.end_game() != "Gagné" and self.end_game() != "Egalité":
            print(self.end_game())
            if self.player_value > self.dealer_value and self.dealer_value >= 17:
                self.has_won = True
                self.game_ended = True
            HIT_or_STAND = input("Voulez vous HIT ou STAND ?")  # A changer pr un bouton cliquable
            if HIT_or_STAND == "HIT":
                self.player_draw()
                self.player_value = self.new_player_value(self.drawed_card)
                print("player new hand", self.player_hand)
                print("player new values", self.player_value)
            if HIT_or_STAND == "STAND":
                while self.dealer_value <= 17:
                    print("miaou")
                    self.dealer_draw()
                    self.dealer_value = self.new_dealer_value(self.dealer_drawed_card)
                    print("new main du croupier : ", self.dealer_hand)
                    print("new valeur du croupier : ", self.dealer_value)

