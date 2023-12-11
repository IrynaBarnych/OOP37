import pickle
#створення об'єкту для серелізації
data = {"name": "Valera", "age": 30, "city": "New York"}
# сералізація об'єкта в байтовий потік
serialized_data = pickle.dumps(data) #перегляд
print(serialized_data)
# через контекстний менеджер
with open("serialized_data.pickle", "wb") as file:
    pickle.dump(data, file)

#десеріалізація
deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)
# через контекстний менеджер
with open("serialized_data.pickle", "rb") as file:
    deserialized_data_file = pickle.load(file)
print(deserialized_data_file)
