# Завдання 2
# Маємо певний словник з назвами музичних груп (виконавців) та альбомів.
# Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження
# даних (використовуючи стиснення та розпакування).


import pickle
import gzip

music_groups_albums = {
    'The Beatles': 'Abbey Road',
    'Queen': 'A Night at the Opera',
    'Led Zeppelin': 'IV',
    'Pink Floyd': 'The Dark Side of the Moon',
    'Metallica': 'Metallica',
    'U2': 'The Joshua Tree',
    'Nirvana': 'Nevermind',
    'Coldplay': 'A Rush of Blood to the Head',
    'Radiohead': 'OK Computer',
    'Foo Fighters': 'The Colour and the Shape'
}


def save_data():
    global music_groups_albums
    with gzip.open("music_groups_albums.pickle.gz", "wb") as file:
        pickle.dump(music_groups_albums, file, protocol=pickle.HIGHEST_PROTOCOL)
    print("Дані збережено!")

def load_data():
    global music_groups_albums
    try:
        with gzip.open("music_groups_albums.pickle.gz", "rb") as file:
            music_groups_albums = pickle.load(file)
        print("Дані завантажено!")
    except FileNotFoundError:
        print("Файл не знайдено.")


def add_group():
    global music_groups_albums
    group = input("Введіть назву музичної групи: ")
    album = input("Введіть назву альбому: ")
    music_groups_albums[group] = album
    print(f"{group} та їх альбом {album} додано.")


def remove_group():
    global music_groups_albums
    group = input("Введіть назву музичної групи для видалення: ")
    if group in music_groups_albums:
        del music_groups_albums[group]
        print(f"{group} видалено.")
    else:
        print(f"{group} не знайдено в словнику.")


def search_album():
    global music_groups_albums
    group = input("Введіть назву музичної групи для пошуку альбому: ")
    album = music_groups_albums.get(group)
    if album:
        print(f"Альбом {group}: {album}")
    else:
        print(f"{group} не знайдено в словнику.")


def edit_album():
    global music_groups_albums
    group = input("Введіть назву музичної групи для редагування альбому: ")
    if group in music_groups_albums:
        new_album = input(f"Введіть новий альбом для {group}: ")
        music_groups_albums[group] = new_album
        print(f"Альбом для {group} змінено на {new_album}.")
    else:
        print(f"{group} не знайдено в словнику.")


def display_menu():
    print("Меню:")
    print("1. Додати музичну групу та альбом")
    print("2. Видалити музичну групу")
    print("3. Пошук альбому за музичною групою")
    print("4. Редагувати альбом музичної групи")
    print("5. Зберегти дані")
    print("6. Завантажити дані")
    print("0. Вийти")


# Приклад використання функцій:
while True:
    display_menu()
    choice = input("Введіть номер опції (0-6): ")

    if choice == "1":
        add_group()
    elif choice == "2":
        remove_group()
    elif choice == "3":
        search_album()
    elif choice == "4":
        edit_album()
    elif choice == "5":
        save_data()
    elif choice == "6":
        load_data()
    elif choice == "0":
        print("Дякую за використання програми. До побачення!")
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")

