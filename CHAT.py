import pyxel



class CHAT:
    def __init__(self ,x ,y ):
        self.money = 1100
        self.doors_unlocked = []
        
        self.x = x
        self.y = y
        self.direction = "haut"

    def dess(self):
        pyxel.image(2).load(0,0,"assets/character/main/" + self.direction + ".png")
        pyxel.blt(self.x, self.y,2,0,0,50,50)


    def mouv(self, lst):
        v = 5
        if pyxel.btn(pyxel.KEY_CTRL):
            v = 1
            
        if pyxel.btn(pyxel.KEY_Z):
            self.direction = "haut"
            if self._peut_bouger(lst, "haut"):
                self.y -= v
        if pyxel.btn(pyxel.KEY_S):
            self.direction = "bas"
            if self._peut_bouger(lst, "bas"):
                self.y += v
        if pyxel.btn(pyxel.KEY_D):
            self.direction = "droite"
            if self._peut_bouger(lst, "droite"):
                self.x += v
        if pyxel.btn(pyxel.KEY_Q):
            self.direction = "gauche"
            if self._peut_bouger(lst, "gauche"):
                self.x -= v
    
    
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
                    x = porte.coord['x'] + 90 // 2
                    y = porte.coord['y']
                else:
                    x = porte.coord['x']
                    y = porte.coord['y'] + 90 // 2
                return x, y
                    