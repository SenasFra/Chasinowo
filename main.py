import pyxel
import salles
import rush
import pygame

pygame.init()
pygame.mixer.music.load("assets/Musiques/Nouveau_projet.mp3")
pygame.mixer.music.play(-1)

class casino:
    def __init__(self):
        pyxel.init(1392, 784)
        self.salle = salles.Debut()
        self.perso = rush.Rush(650,425)
        self.jeu = ""
        pyxel.run(self.update, self.draw)

    def update(self):
        self.perso.mouv(self.salle.mur)
        if len(self.salle.porte_bas)==3:
            if self.perso.x >= self.salle.porte_bas[0] and self.perso.x <= self.salle.porte_bas[1] and self.perso.y == self.salle.porte_bas[2] and pyxel.btnp(pyxel.KEY_E):
                self.salle = self.salle.changer_bas()
                self.perso.x = self.salle.porte_haut[0]
                self.perso.y = self.salle.mur[1]
        if len(self.salle.porte_haut)==3:
            if self.perso.x >= self.salle.porte_haut[0] and self.perso.x <= self.salle.porte_haut[1] and self.perso.y == self.salle.porte_haut[2] and pyxel.btnp(pyxel.KEY_A):
                self.salle = self.salle.changer_haut()
                self.perso.x = self.salle.porte_bas[0]
                self.perso.y = self.salle.mur[3]
        if pyxel.btnp(pyxel.KEY_K):
            print(self.perso.x,self.perso.y) 

    def draw(self):
        self.salle.dess()
        self.perso.dess()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    casino()