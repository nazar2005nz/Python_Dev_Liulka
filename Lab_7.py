# Введення даних
numbers = [10, 20, 30, 40, 50]
tuple_numbers = tuple(numbers)  # Створюємо кортеж зі списку
n = int(input("Введіть число n: "))

# Використання генератора списків
result = [num for num in tuple_numbers if num < n]

# Вивід результату
print(f"Числа, менші за {n}: {result}")

# Створення кортежу
tuple_strings = ("apple", "banana", "cherry")

# Об'єднання рядків з комою
result = ", ".join(tuple_strings)

# Вивід результату
print(result)

# Створення словника
books = {
    "1984": {"Автор": "Джордж Орвелл", "Рік видання": 1949, "Кількість сторінок": 328},
    "Майстер і Маргарита": {"Автор": "Михайло Булгаков", "Рік видання": 1967, "Кількість сторінок": 384},
    "Портрет Доріана Грея": {"Автор": "Оскар Уайльд", "Рік видання": 1890, "Кількість сторінок": 254},
}

# Введення назви книги
book_name = input("Введіть назву книги: ")

# Вивід інформації про книгу
if book_name in books:
    book_info = books[book_name]
    print(f"Автор: {book_info['Автор']}, Рік видання: {book_info['Рік видання']}, Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print("Такої книги немає у бібліотеці.")

# Створення словника
students = {
    "Іванов": ("Іван", "Математика: 80", "Фізика: 75"),
    "Петров": ("Петро", "Математика: 90", "Фізика: 85"),
    "Сидоров": ("Сидір", "Математика: 70", "Фізика: 65"),
}

# Введення прізвища студента
last_name = input("Введіть прізвище студента: ")

# Вивід інформації
if last_name in students:
    student_info = students[last_name]
    print(f"Ім'я: {student_info[0]}")
    for subject in student_info[1:]:
        print(subject)
else:
    print("Такого студента немає.")

# Створення словника
phone_book = {
    "Іван": ["+380123456789", "+380987654321"],
    "Петро": ["+380112233445"],
    "Марія": ["+380998877665", "+380334455667"]
}

# Функція для додавання номера телефону
def add_phone(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
    else:
        phone_book[contact_name] = [phone_number]

# Додавання нового номера
contact = input("Введіть ім'я контакту: ")
number = input("Введіть номер телефону: ")
add_phone(contact, number)

# Вивід списку номерів телефону
for name, phones in phone_book.items():
    print(f"{name}: {', '.join(phones)}")

