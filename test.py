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
    number_str = str(number)  # convert number to string
    digits = len(number_str)
    if digits <= 3:
        return number_str
    elif digits % 3 == 0:
        separator = " "
        groups = digits // 3
    else:
        separator = " "
        groups = digits // 3 + 1
    result = ""
    for i in range(groups):
        start = digits - (i + 1) * 3
        end = digits - i * 3
        if start < 0:
            start = 0
        result = separator + number_str[start:end] + result
    return result.strip()

print(separate_digits(112135))