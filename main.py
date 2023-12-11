"""Завдання 3
Маємо певний словник з логінами і паролями користувачів.
Логін використовується як ключ, пароль —
як значення. Реалізуйте: додавання, видалення, пошук,
редагування, збереження та завантаження даних
(використовуючи стиснення та розпакування)."""
import pickle
import gzip
user_credentials = {}
#збереження
def save_data():
    global user_credentials
    with gzip.open("credentials.pickle.gz", "wb") as file:
        pickle.dump(user_credentials, file, protocol=pickle.HIGHEST_PROTOCOL)
    print("Дані збережено!")
#завантаження даних
def load_data():
    global user_credentials
    try:
        with gzip.open("credentials.pickle.gz", "rb") as file:
           user_credentials = pickle.load(file)
        print("Дані завантажено!")
    except FileNotFoundError:
        print("Файл не знайдено.")
#додавання
def add_user():
    global user_credentials
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    user_credentials[login] = password
    print("Користувача додано")
add_user()
save_data()
load_data()
print(user_credentials)

