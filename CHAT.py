import pyxel
from assets.character.main.haut import Haut
from assets.character.main.droite import Droite
from assets.character.main.bas import Bas
from assets.character.main.gauche import Gauche
from assets.character.main.sitting import Sitting

class CHAT:
    def __init__(self ,x ,y ):
        self.money = 20000000
        self.doors_unlocked = ["1-5", "5-1", "D-3", "3-D"]
        self.assis = False
        self.x = x
        self.y = y
        self.direction = "haut"
        self.base = Haut()

    def dess(self):
        self.base.dess(self.x, self.y)

    def mouv(self, lst):
        if self.assis == False:
            v = 5
            if pyxel.btn(pyxel.KEY_CTRL):
                v = 1
            if pyxel.btn(pyxel.KEY_Z):
                #self.direction = "haut"
                self.base = Haut()
                if self._peut_bouger(lst, "haut"):
                    self.y -= v
            if pyxel.btn(pyxel.KEY_S):
                #self.direction = "bas"
                self.base = Bas()
                if self._peut_bouger(lst, "bas"):
                    self.y += v
            if pyxel.btn(pyxel.KEY_D):
                #self.direction = "droite"
                self.base = Droite()
                if self._peut_bouger(lst, "droite"):
                    self.x += v
            if pyxel.btn(pyxel.KEY_Q):
                #self.direction = "gauche"
                self.base = Gauche()
                if self._peut_bouger(lst, "gauche"):
                    self.x -= v
        else:
            self.base = Sitting()
    
    
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
                
                
    def replace_cat(self, room, previous_door_name):
        reversed_name = ""
        for l in reversed(previous_door_name):
            reversed_name += l
            
        for porte in room.portes:
            if porte.name == reversed_name:
                if porte.is_in_front:
                    x = porte.coord['x'] + porte.size // 2
                    y = porte.coord['y']
                else:
                    x = porte.coord['x']
                    y = porte.coord['y'] + porte.size // 2
                return x, y
                    