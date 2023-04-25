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

temp = time.time()
        
while time.time() - temp < 1:
    print(time.time() - temp)