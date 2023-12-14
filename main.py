# Завдання 1
# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення.
# Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).


import pickle
import gzip

countries_capitals = {
    'Австрія': 'Відень',
    'Албанія': 'Тирана',
    'Андорра': 'Андорра-ла-Велья',
    'Бельгія': 'Брюссель',
    'Болгарія': 'Софія',
    'Боснія і Герцеговина': 'Сараєво',
    'Ватикан': 'Ватикан',
    'Велика Британія': 'Лондон',
    'Греція': 'Афіни',
    'Данія': 'Копенгаген',
    'Естонія': 'Таллінн',
    'Ірландія': 'Дублін',
    'Ісландія': 'Рейк\'явік',
    'Іспанія': 'Мадрид',
    'Італія': 'Рим',
    'Косово': 'Приштина',
    'Латвія': 'Рига',
    'Литва': 'Вільнюс',
    'Ліхтенштейн': 'Вадуц',
    'Люксембург': 'Люксембург',
    'Мальта': 'Валлетта',
    'Молдова': 'Кишинів',
    'Німеччина': 'Берлін',
    'Норвегія': 'Осло',
    'Північна Македонія': 'Скоп\'є',
    'Польща': 'Варшава',
    'Португалія': 'Лісабон',
    'Румунія': 'Бухарест',
    'Сан-Марино': 'Сан-Марино',
    'Сербія': 'Белград',
    'Словаччина': 'Братислава',
    'Словенія': 'Любляна',
    'Угорщина': 'Будапешт',
    'Україна': 'Київ',
    'Фінляндія': 'Гельсінкі',
    'Франція': 'Париж',
    'Хорватія': 'Загреб',
    'Чехія': 'Прага',
    'Чорногорія': 'Подгориця',
    'Швейцарія': 'Берн',
    'Швеція': 'Стокгольм'
}

# Збереження даних
def save_data():
    global countries_capitals
    with gzip.open("countries_capitals.pickle.gz", "wb") as file:
        pickle.dump(countries_capitals, file, protocol=pickle.HIGHEST_PROTOCOL)
    print("Дані збережено!")

# Завантаження даних
def load_data():
    global countries_capitals
    try:
        with gzip.open("countries_capitals.pickle.gz", "rb") as file:
            countries_capitals = pickle.load(file)
        print("Дані завантажено!")
    except FileNotFoundError:
        print("Файл не знайдено.")

# Додавання країни і столиці
def add_country():
    global countries_capitals
    country = input("Введіть назву країни: ")
    capital = input("Введіть назву столиці: ")
    countries_capitals[country] = capital
    print(f"{country} та її столицю {capital} додано.")

# Видалення країни і столиці
def remove_country():
    global countries_capitals
    country = input("Введіть назву країни для видалення: ")
    if country in countries_capitals:
        del countries_capitals[country]
        print(f"{country} видалено.")
    else:
        print(f"{country} не знайдено в словнику.")

# Пошук столиці за назвою країни
def search_capital():
    global countries_capitals
    country = input("Введіть назву країни для пошуку столиці: ")
    capital = countries_capitals.get(country)
    if capital:
        print(f"Столиця {country}: {capital}")
    else:
        print(f"{country} не знайдено в словнику.")

# Редагування столиці за назвою країни
def edit_capital():
    global countries_capitals
    country = input("Введіть назву країни для редагування столиці: ")
    if country in countries_capitals:
        new_capital = input(f"Введіть нову столицю для {country}: ")
        countries_capitals[country] = new_capital
        print(f"Столицю {country} змінено на {new_capital}.")
    else:
        print(f"{country} не знайдено в словнику.")



def menu():
    while True:
        print("\nМеню:")
        print("1. Додати країну та столицю")
        print("2. Видалити країну та столицю")
        print("3. Пошук столиці за назвою країни")
        print("4. Редагувати столицю за назвою країни")
        print("5. Зберегти дані")
        print("6. Завантажити дані")
        print("7. Вийти")

        choice = input("Виберіть опцію (1-7): ")

        if choice == "1":
            add_country()
        elif choice == "2":
            remove_country()
        elif choice == "3":
            search_capital()
        elif choice == "4":
            edit_capital()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

# Приклад використання:
menu()

# Приклад використання функцій:
add_country()
save_data()
load_data()
print(countries_capitals)

search_capital()
edit_capital()
remove_country()
save_data()
load_data()
print(countries_capitals)