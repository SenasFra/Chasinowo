import pyxel

class Rush:
    def __init__(self ,x ,y ):
        self.x = x
        self.y = y

    def dess(self):
        pyxel.rect(self.x,self.y,50,50,0)

    def mouv(self, lst):
        v = 8
        if pyxel.btn(pyxel.KEY_D) and self.x < lst[2]:
            if self.x + v <lst[2]:
                self.x += v
            else:
                self.x += lst[2]-self.x
        if pyxel.btn(pyxel.KEY_Q) and self.x > lst[0]:
            if self.x - v > lst[0]:
                self.x -= v
            else:
                self.x -= self.x -lst[0]
        if pyxel.btn(pyxel.KEY_Z)and self.y > lst[1]:
            if self.y - v > lst[1]:
                self.y -= v
            else:
                self.y -= self.y -lst[1]
        if pyxel.btn(pyxel.KEY_S)and self.y < lst[3]:
            if self.y + v < lst[3]:
                self.y += v
            else:
                self.y += lst[3] - self.y