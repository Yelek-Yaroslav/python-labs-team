def file_error_check(e):
    # Єлек: функція для обробки помилок, що можуть виникати під час роботи з файлами
    if isinstance(e, FileNotFoundError):
        print("Помилка: файл не знайдено.")
    elif isinstance(e, PermissionError):
        print("Помилка: відсутні права доступу до файлу.")
    elif isinstance(e, IOError):
        print("Помилка введення/виведення при роботі з файлом.")
    else:
        print(f"Невідома помилка: {e}")


def file_create_and_answer1():
    # Єлек: функція створює новий текстовий файл і записує в нього питання для наступного студента
    try:
        # створюємо файл з кодуванням UTF-8, щоб підтримувалася кирилиця
        with open("team_file.txt", "w", encoding="utf-8") as file:
            file.write("Студент 1: Єлек Ярослав\n")
            file.write("1. Які основні режими відкриття файлів у Python і чим вони відрізняються?\n\n")
        print("Студент 1: файл успішно створено та записано питання.")
    except Exception as e:
        # якщо виникає помилка, викликаємо функцію обробки виключень
        file_error_check(e)

def file_answer2():
    # Крячко Артем: функція додає свою відповідь на питання та ставить нове питання 
    try:
        with open("team_file.txt", "a", encoding="utf-8") as file:
            file.write("Студент 2: Іваненко Петро\n")
            file.write("Відповідь на питання 1:\n")
            file.write("У Python є такі основні режими відкриття файлів:\n")
            file.write("r - читання (файл має існувати)\n")
            file.write("w - запис (файл створюється або перезаписується)\n")
            file.write("a - додавання (нові дані додаються в кінець файлу)\n")
            file.write("r+ - читання та запис\n\n")
            # нове питання
            file.write("2. Яким чином у Python можна обробляти виключення при роботі з файлами?\n\n")
        print("Студент 2: відповідь додана та поставлено нове питання.")
    except Exception as e:
        file_error_check(e)

file_answer2()


file_create_and_answer1()
file_answer2()
