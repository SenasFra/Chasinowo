import pyxel
from haut import Haut
from droite import Droite
from gauche import Gauche
from bas import Bas

class Rush:
    def __init__(self ,x ,y ):
        self.x = x
        self.y = y
        self.direction = "haut"
        self.base = Haut()

    def dess(self):
        self.base.dess(self.x,self.y)


    def mouv(self, lst):
        if pyxel.btn(pyxel.KEY_CTRL):
            v = 1
        else:
            v = 5
        if pyxel.btn(pyxel.KEY_Z) and self._peut_bouger(lst, "haut"):
            self.y -= v
            self.base = Haut()
        if pyxel.btn(pyxel.KEY_S) and self._peut_bouger(lst, "bas"):
            self.y += v
            self.base = Bas()
        if pyxel.btn(pyxel.KEY_D) and self._peut_bouger(lst, "droite"):
            self.x += v
            self.base = Droite()
        if pyxel.btn(pyxel.KEY_Q) and self._peut_bouger(lst, "gauche"):
            self.x -= v
            self.base = Gauche()
    
    
    def _peut_bouger(self, lst, direction):
        if direction == "droite":
            if self.x < lst[0][2]:
                for k in range (1,len(lst)):
                    if lst[k][1] < self.y < lst[k][3] and lst[k][0]-10 < self.x < lst[k][2]:
                        return False
                return True
        elif direction == "gauche":
            if self.x > lst[0][0]:
                for k in range (1,len(lst)):
                    if lst[k][1] < self.y < lst[k][3] and lst[k][0] < self.x < lst[k][2]+10:
                        return False
                return True
        elif direction == "haut":
            if self.y > lst[0][1]:
                for k in range (1,len(lst)):
                    if lst[k][0] < self.x < lst[k][2] and lst[k][1] < self.y < lst[k][3]+10:
                        return False
                return True
        elif direction == "bas":
            if self.y < lst[0][3]:
                for k in range (1,len(lst)):
                    if lst[k][0] < self.x < lst[k][2] and  lst[k][1]-10 < self.y < lst[k][3]:
                        return False
                return True
                