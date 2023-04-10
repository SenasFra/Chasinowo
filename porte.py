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
                doors_unlocked.append(self.name)
                return self.next_room()
            
 

    