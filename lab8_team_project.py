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

file_create_and_answer1()
