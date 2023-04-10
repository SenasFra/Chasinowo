class Porte:
    def __init__(self, name: str, coord: dict, price: int, next_room: object, is_in_front: bool):
        self.name = name
        self.coord = coord
        self.price = price
        self.next_room = next_room
        self.is_in_front = is_in_front
        
        
    def enter(self, user_money: int, doors_unlocked: list):
        if self.name in doors_unlocked:
            return self.next_room
        
        if user_money >= self.price:
            user_money -= self.price
            doors_unlocked.append(self.name)
            return self.next_room
            
 

    