n = int(input("Enter a number: "))  # Приймаємо введення від користувача та перетворюємо на ціле число
print(n >= 100)  # Друкуємо результат порівняння

# Введення двох дійсних чисел
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

# Порівняння чисел
if a > b:
    print("Найбільше число:", a)
else:
    print("Найбільше число:", b)

# Введення рядка користувачем
plant_name = input("Enter the name of the plant: ")

# Використання конструкції if-elif-else
if plant_name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant_name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant_name}!")

def calculate_tax(income):
    if income <= 85528:
        tax = income * 0.18 - 556.02
    else:
        tax = 14839.02 + (income - 85528) * 0.32
    return max(0, round(tax, 0))

# Вхід
income = float(input("Enter income: "))
tax = calculate_tax(income)
print(f"The tax is: {tax} thalers")

def check_year(year):
    if year < 1582:
        print("Not within the Gregorian calendar period")
    elif year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

# Вхід
year = int(input("Enter a year: "))
check_year(year)

secret_number = 42  # Це може бути будь-яке число, яке обере фокусник

print("+================================+")
print("| Welcome to my game, muggle!    |")
print("| Enter an integer number        |")
print("| and guess what number I've     |")
print("| picked for you.                |")
print("| So, what is the secret number? |")
print("+================================+")

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print(f"Well done, muggle! Now you're free.")
        break
    else:
        print("Ha-ha! You're stuck in my loop!")

import time

# Рахунок "Міссісіпі"
for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# Оператор break для виходу з циклу
while True:
    user_input = input("Enter a word: ")
    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break

# Пожирач голосних
user_word = input("Enter a word: ").upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

# Покращений пожирач голосних
user_word = input("Enter a word: ").upper()
word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)

# Висота піраміди
blocks = int(input("Enter the number of blocks: "))
height = 0
current_layer_blocks = 1

while blocks >= current_layer_blocks:
    blocks -= current_layer_blocks
    height += 1
    current_layer_blocks += 1

print(f"The height of the pyramid: {height}")

# Гіпотеза Коллатца
n = int(input("Enter a number: "))
steps = 0

while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print(n)
print(f"steps = {steps}")

