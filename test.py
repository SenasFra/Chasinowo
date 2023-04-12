import pickle

money = 5000
doors = ["miaou", "miaou", "miaou"]

data = {
    "money": money,
    "doors_unlocked": doors
}

# Save data to a file
with open('./save/data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Load data from a file
with open('./save/data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)
