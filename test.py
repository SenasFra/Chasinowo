import pickle
import time
import pyxel
# money = 5000
# doors = ["miaou", "miaou", "miaou"]

# data = {
#     "money": money,
#     "doors_unlocked": doors
# }

# # Save data to a file
# with open('./save/data.pickle', 'wb') as f:
#     pickle.dump(data, f)

# # Load data from a file
# with open('./save/data.pickle', 'rb') as f:
#     loaded_data = pickle.load(f)
#     print(loaded_data)


# import pyxel
# from assets.font.PyxelUnicode import PyxelUnicode

# pyxel.init(256, 256)
# pyxel.cls(0)

# font_path = "assets/font/pixelmix.ttf"

# y = 0
# # check how it looks like when the size are [8,10,12,14,16.....]
# for s in range(8,36, 2):
#     pyuni = PyxelUnicode(font_path, original_size=s)
#     pyxel.text(0, y, str(s), 7)
#     pyuni.text(10, y, s='DUMMY TEXT, dummy text.')
#     y += pyuni.font_height

# pyxel.show()

# import asyncio

# def wait():
#     print("miaou")
#     return True

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1, result=wait())
#     print('... World!')

# asyncio.run(main())
# import threading

# def do_something():
#     # do some time-consuming task here
#     print("miaou")

# # Define a function to run the timeout thread
# def timeout():
#     global timer_expired
#     timer_expired = False
#     timer = threading.Timer(1, handle_timeout) # Timeout after 10 seconds
#     timer.start()
#     timer.join()
#     if timer_expired:
#         raise Exception("Time's up!")
#     else:
#         timer.cancel()

# # Define a function to handle the timeout
# def handle_timeout():
#     global timer_expired
#     timer_expired = True

# # Start the timeout thread and run the function
# timer_expired = False
# timeout_thread = threading.Thread(target=timeout)
# timeout_thread.start()

# do_something()

# # Wait for the timeout thread to finish
# timeout_thread.join()

def add_spaces_between_number(money):
        money = str(money)
        reversed_result = ""
        #trouve où il faut mettre les espace
        for i in range(len(str(money)) - 1, -1, -1):
            print(i)
            reversed_result += money[i]
            if (i+1) % 3 == 0:
                reversed_result += " "
        #remet les chiffres dans le bon ordre
        result = ""
        for l in reversed(reversed_result):
            result += l
        
        return result
    
print(add_spaces_between_number("120500"))

def separate_digits(number):
    number_str = str(number)
    number_length = len(number_str)
    
    #renvoie directement le nombre si il a moins de 3 chiffres
    if number_length <= 3:
        return number_str
    #si le nombre est un mutliple de 3, calcule le nombre de groupes de 3 chiffres dans celui-ci
    elif number_length % 3 == 0:
        groups_of_3 = number_length // 3
    #de même s'il n'est pas un multiple de 3 sauf qu'on rajoute 1 pour prendre en compte les chiffres restants
    else:
        groups_of_3 = number_length // 3 + 1
        
    space = " "
    result = ""
    
    # Pour chaque groupe de trois chiffres dans le nombre, ajoute un espace et les chiffres à la variable de résultat
    # en partant de la fin du nombre pour traiter les chiffres dans l'ordre correct
    for i in range(groups_of_3):
        start = number_length - (i + 1) * 3
        end = number_length - i * 3
        #si le groupe de 3 traité est plus petit que 3 chiffres, on change la variable à 0 pour prendre en compte les chiffres restants
        if start < 0:
            start = 0
        result = space + number_str[start:end] + result #ajoute un espace et les chiffres du groupe traité
    #supprime les espaces sur les côtés donc celui intiale
    return result.strip()

print(separate_digits(89653352153))

bets = [9, 4]
result = 10
premier = (result in range(bets[1], bets[0] + 1))
second = (result in range(bets[0], bets[1] + 1))

print(premier, second)