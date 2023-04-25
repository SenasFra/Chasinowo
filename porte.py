#classe qui permet de créer le système de porte (quand on traverse une porte, on change de salle)
class Porte:
    def __init__(self, name: str, coord: dict, price: int, money_condition: int, next_room: object, is_in_front: bool, size:  int):
        self.name = name
        self.coord = coord
        self.price = price
        self.money_condition = money_condition
        self.next_room = next_room
        self.is_in_front = is_in_front
        self.size = size
        
        self.chatbox = None
        
    def enter(self, CHAT: object):
        #si la porte est débloqué, on change directement de salle
        if self.name in CHAT.doors_unlocked:
            return self.next_room

    
    
            
 

    