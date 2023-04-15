class Porte:
    def __init__(self, name: str, coord: dict, price: int, next_room: object, is_in_front: bool, size:  int):
        self.name = name
        self.coord = coord
        self.price = price
        self.next_room = next_room
        self.is_in_front = is_in_front
        self.size = size
        
        
    def enter(self, CHAT: object):
        if self.name in CHAT.doors_unlocked:
            return self.next_room
        
        if CHAT.money >= self.price:
            CHAT.money -= self.price
            CHAT.doors_unlocked.append(self.name)
            return self.next_room
        
            
 

    