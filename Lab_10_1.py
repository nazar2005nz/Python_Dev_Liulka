def is_palindrome(text):
    # Перетворюємо текст на нижній регістр та видаляємо пробіли
    text = text.lower().replace(" ", "")
    # Перевіряємо, чи однаковий текст у прямому та зворотному порядках
    return text == text[::-1]

# Введення тексту користувачем
text = input("Введіть текст: ")
if text.strip() == "":
    print("Empty string is not a palindrome.")
else:
    if is_palindrome(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

def are_anagrams(text1, text2):
    # Приводимо тексти до нижнього регістру, видаляємо пробіли та сортуємо літери
    text1 = sorted(text1.lower().replace(" ", ""))
    text2 = sorted(text2.lower().replace(" ", ""))
    return text1 == text2

# Введення текстів користувачем
text1 = input("Введіть перше слово: ")
text2 = input("Введіть друге слово: ")

if text1.strip() == "" or text2.strip() == "":
    print("Empty strings are not anagrams.")
else:
    if are_anagrams(text1, text2):
        print("Anagrams")
    else:
        print("Not anagrams")

def calculate_life_number(birth_date):
    # Підсумовуємо всі цифри дати народження
    while len(birth_date) > 1:
        birth_date = str(sum(int(digit) for digit in birth_date))
    return int(birth_date)

# Введення дати народження
birth_date = input("Введіть дату народження у форматі YYYYMMDD: ").strip()
if birth_date.isdigit():
    print("Цифра життя:", calculate_life_number(birth_date))
else:
    print("Error: введено неправильний формат дати.")

def is_hidden(word, sequence):
    # Ітеративно шукаємо кожну літеру з `word` у `sequence`
    index = 0
    for char in word.lower():
        index = sequence.lower().find(char, index)
        if index == -1:
            return False
        index += 1
    return True

# Введення даних користувачем
word = input("Введіть слово: ")
sequence = input("Введіть послідовність символів: ")

if is_hidden(word, sequence):
    print("Yes")
else:
    print("No")

while True:
    try:
        value = int(input("Введіть ціле число: "))
        print(value / 2)
        break
    except ValueError:
        print("Введене значення не є допустимим числом. Повторіть спробу...")


def calculate_life_number(birth_date):
    # Підсумовуємо всі цифри дати народження
    while len(birth_date) > 1:
        birth_date = str(sum(int(digit) for digit in birth_date))
    return int(birth_date)


while True:
    try:
        # Введення дати народження
        birth_date = input("Введіть дату народження у форматі YYYYMMDD: ").strip()
        # Перевіряємо, чи рядок містить лише цифри
        if not birth_date.isdigit():
            raise ValueError("Дата повинна складатися тільки з цифр.")
        # Перевіряємо, чи довжина дати відповідає формату YYYYMMDD
        if len(birth_date) != 8:
            raise ValueError("Дата повинна містити рівно 8 цифр.")

        # Розрахунок і вивід цифри життя
        print("Цифра життя:", calculate_life_number(birth_date))
        break
    except ValueError as e:
        print(f"Error: {e} Повторіть спробу.")

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: the value is not within permitted range ({min_val}..{max_val})")
        except ValueError:
            print("Error: wrong input")

# Використання функції
number = get_valid_number("Введіть ціле число: ", 1, 10)
print(f"Ви ввели допустиме число: {number}")
