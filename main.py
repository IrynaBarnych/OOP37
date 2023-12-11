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

### приклад стиснення інформації
import gzip
with gzip.open('compressed_file.gz', "wb") as file:
    file.write(b"some text")

#  ще один з видів стискання
data = b"some text"
compressed_data = gzip.compress(data)
print(compressed_data)

# розпакування стиснених даних
decompressed_data = gzip.decompress(compressed_data)
print(decompressed_data)

#розпакування з файлу
with gzip.open('compressed_file.gz', "rb") as file:
    new_data = file.read()
print(new_data)


from zipfile import ZipFile
with ZipFile('metanit.zip', "a") as myzip:
    myzip.write("eggs.txt")
    myzip.write("serialized_data.pickle")

