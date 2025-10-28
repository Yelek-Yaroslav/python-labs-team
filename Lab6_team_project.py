students = {
    "Єлек Ярослав Юрійович": {
        'Група': "Кн-41.2",
        'Курс': 2,
        'Предмети та оцінки за ІІ семестр': {
            "Чисельні методи": 86,
            "Вища математика": 89,
            "Програмування": 92
        }
    },
    "Крячко Артем": {
        'Група': "Кн-41.2",
        'Курс': 2,
        'Предмети та оцінки за ІІ семестр': {
            "Чисельні методи": 95,
            "Вища математика": 87,
            "Програмування": 95
        }
    },
    "Басанець Єгор Юрійович": {
        'Група': "Кн-41.2",
        'Курс': 2,
        'Предмети та оцінки за ІІ семестр': {
            "Чисельні методи": 96,
            "Вища математика": 98,
            "Програмування": 92
        }
    },
    "Шевельов Артем": {
        'Група': "Кн-41.1",
        'Курс': 2,
        'Предмети та оцінки за ІІ семестр': {
            "Чисельні методи": 92,
            "Вища математика": 89,
            "Програмування": 95
        }
    }
}

#Функція Єлек Я.Ю.
#Функція для додавання нового студента до словника.
def add_student():

    name = input("Введіть прізвище, ім'я та по батькові: ").strip()
    group = input("Введіть номер групи: ").strip()

    # перевірка, щоб курс був числом
    try:
        course = int(input("Введіть курс: "))
    except ValueError:
        print("Курс має бути числом! Спробуйте ще раз.")
        return

    subjects_grades = {}

    # цикл для введення предметів і оцінок
    while True:
        subject = input("Введіть назву предмету (для завершення натисніть Enter): ").strip()
        if not subject:
            break
        try:
            grade = int(input(f"Введіть оцінку за '{subject}': "))
            if 0 <= grade <= 100:
                subjects_grades[subject] = grade
            else:
                print("Оцінка має бути від 0 до 100.")
        except ValueError:
            print("Введіть числове значення оцінки!")

    # перевірка, чи студент уже існує
    if name in students:
        print(f"️Студент {name} вже є у словнику.")
    else:
        students[name] = {
            'Група': group,
            'Курс': course,
            'Предмети та оцінки за ІІ семестр': subjects_grades
        }
        print(f"\Студента {name} успішно додано!")
        print("Його дані:")
        for key, value in students[name].items():
            print(f"  {key}: {value}")

# Функція для виведення інформації про всіх студентів
def display_all_students():
    print("\nСписок студентів:")

    if not students:
        print("Список студентів порожній.")
        return

    for full_name, info in students.items():
        print(f"\nПІБ: {full_name}")
        print(f"Група: {info['Група']}")
        print(f"Курс: {info['Курс']}")
        print("Предмети та оцінки за ІІ семестр:")
        for subject, grade in info['Предмети та оцінки за ІІ семестр'].items():
            print(f"  {subject}: {grade}")


def display_sorted_students_by_name():
    print("\n--- Список студентів (відсортований за ПІБ) ---")
    sorted_names = sorted(students.keys())
    for full_name in sorted_names:
        info = students[full_name]
        print(f"\nПІБ: {full_name}")
        print(f"Група: {info['Група']}")
        print(f"Курс: {info['Курс']}")
        print("Предмети та оцінки за ІІ семестр (відсортовані):")
        sorted_subjects = sorted(info['Предмети та оцінки за ІІ семестр'].items())
        for subject, grade in sorted_subjects:
                    print(f"  {subject}: {grade}")

add_student()
display_all_students()
display_sorted_students_by_name()


# Завдання для наступного студента: розробити функцію сортування даних у словнику.
