import pickle

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

import asyncio

def wait():
    print("miaou")

async def main():
    print('Hello ...')
    await asyncio.sleep(1, result=wait())
    print('... World!')

asyncio.run(main())