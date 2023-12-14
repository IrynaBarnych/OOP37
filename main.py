# Завдання 2
# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.

import pickle
import gzip

user_credentials = []

# Збереження даних
def save_data():
    global user_credentials
    with gzip.open("credentials.pickle.gz", "wb") as file:
        pickle.dump(user_credentials, file, protocol=pickle.HIGHEST_PROTOCOL)
    print("Дані збережено!")

# Завантаження даних
def load_data():
    global user_credentials
    try:
        with gzip.open("credentials.pickle.gz", "rb") as file:
            user_credentials = pickle.load(file)
        print("Дані завантажено!")
    except FileNotFoundError:
        print("Файл не знайдено.")

# Додавання даних
def add_user():
    global user_credentials
    login = input("Введіть логін нового користувача: ")
    password = input("Введіть пароль: ")
    user_credentials.append((login, password))
    print(f"Користувача {login} додано.")

# Видалення користувача
def remove_user():
    global user_credentials
    login_to_remove = input("Введіть логін користувача, якого потрібно видалити: ")
    user_credentials = [user for user in user_credentials if user[0] != login_to_remove]
    print(f"Користувача з логіном {login_to_remove} видалено.")

# Головне меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання даних")
        print("4. Видалення даних")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            load_data()
        elif choice == '2':
            save_data()
        elif choice == '3':
            add_user()
        elif choice == '4':
            remove_user()
        elif choice == '5':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск головного меню
main_menu()
