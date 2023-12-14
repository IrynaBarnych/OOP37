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
# Видалення користувача
def remove_user():
    global user_credentials
    login_to_remove = input("Введіть логін користувача, якого потрібно видалити: ")
    if login_to_remove in user_credentials:
        del user_credentials[login_to_remove]
        print(f"Користувача з логіном {login_to_remove} видалено.")
    else:
        print(f"Користувача з логіном {login_to_remove} не знайдено.")

# Пошук користувача
def find_user():
    global user_credentials
    login_to_find = input("Введіть логін користувача, якого потрібно знайти: ")
    if login_to_find in user_credentials:
        print(f"Користувач з логіном {login_to_find} знайдено. Пароль: {user_credentials[login_to_find]}")
    else:
        print(f"Користувача з логіном {login_to_find} не знайдено.")

# Редагування паролю користувача
def edit_password():
    global user_credentials
    login_to_edit = input("Введіть логін користувача, пароль якого потрібно змінити: ")
    if login_to_edit in user_credentials:
        new_password = input("Введіть новий пароль: ")
        user_credentials[login_to_edit] = new_password
        print(f"Пароль користувача з логіном {login_to_edit} змінено.")
    else:
        print(f"Користувача з логіном {login_to_edit} не знайдено.")


# Меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Додати користувача")
        print("2. Видалити користувача")
        print("3. Знайти користувача")
        print("4. Редагувати пароль користувача")
        print("5. Зберегти дані")
        print("6. Завантажити дані")
        print("7. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            remove_user()
        elif choice == '3':
            find_user()
        elif choice == '4':
            edit_password()
        elif choice == '5':
            save_data()
        elif choice == '6':
            load_data()
        elif choice == '7':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск головного меню
main_menu()

# Додавання користувача
add_user()

# Збереження даних
save_data()

# Завантаження даних
load_data()

# Видалення користувача
remove_user()

# Пошук користувача
find_user()

# Редагування паролю користувача
edit_password()

# Виведення збережених користувачів
print(user_credentials)

