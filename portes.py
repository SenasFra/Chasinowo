import salles

class Porte:
    def __init__(self, name: str, coord: dict, price: int, next_room: object):
        self.name = name
        self.coord = coord
        self.price = price
        self.next_room = next_room
        
        
    def Enter(self, user_money: int, doors_unlocked: list):
        if self.name not in doors_unlocked:
            if user_money >= self.price:
                user_money -= self.price
                return self.next_room
            



def move(x, y):
    pass
 
Porte_D_1 = ("D-1", {'x': 270, 'y': 295}, 1000, "")
Porte_D_2 = ("D-2", {'x': 630, 'y': 140}, 1000, "")
Porte_D_3 = ("D-3", {'x': 1025, 'y': 300}, 0, "")
Porte_D_F = ("D-F", {'x': 650, 'y': 500}, 1000000, "")
    