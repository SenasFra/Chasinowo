import pickle

def save(CHAT, current_room):
    try:
        with open('save/data.pickle', 'wb') as f:
            pickle.dump([CHAT.money, CHAT.doors_unlocked, [CHAT.x, CHAT.y], current_room], f)
    except:
        pass