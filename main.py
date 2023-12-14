# Завдання 1
# Користувач заповнює з клавіатури список цілих.
# Стисніть отримані дані та збережіть їх у файл. Після цього
# завантажте дані з файлу в новий список.

import pickle
import gzip

# збереження списку у файл
def save_list_to_file(data_list):
    with gzip.open('data_list.pickle.gz', 'wb') as file:
        pickle.dump(data_list, file, protocol=pickle.HIGHEST_PROTOCOL)
    print("Дані збережено.")

# завантаження списку з файлу та повернення його
def load_list_from_file():
    try:
        with gzip.open('data_list.pickle.gz', 'rb') as file:
            loaded_list = pickle.load(file)
        print("Дані завантажено.")
        return loaded_list
    except FileNotFoundError:
        print("Файл із даними не знайдено.")
        return None

user_input = input("Введіть список цілих чисел через пробіл: ")

user_list = [int(num) for num in user_input.split()]

if user_list:
    save_list_to_file(user_list)
    print("Введені дані:", user_list)
else:
    print("Немає даних для збереження.")

loaded_list = load_list_from_file()

if loaded_list:
    print("Завантажені дані:", loaded_list)