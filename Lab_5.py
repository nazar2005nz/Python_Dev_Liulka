# Крок 1: Замінити число в списку
numbers = [1, 2, 3, 4, 5]
index = int(input("Enter the index to replace (0-4): "))
value = int(input("Enter the new value: "))
numbers[index] = value

# Крок 2: Видалити останній елемент
numbers.pop()

# Крок 3: Вивести довжину списку
print("Updated list:", numbers)
print("Length of the list:", len(numbers))

# Реалізація сортування методом бульбашки
numbers = [34, 23, 7, 1, 0]
n = len(numbers)

for i in range(n - 1):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

# Видалення дублікатів
original_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for number in original_list:
    if number not in unique_list:
        unique_list.append(number)

print("The list with unique elements only:", unique_list)

# Створення шахівниці
board = [["_"] * 8 for _ in range(8)]

# Розставлення тур у кутах
board[0][0] = "R"  # Верхній лівий
board[0][7] = "R"  # Верхній правий
board[7][0] = "R"  # Нижній лівий
board[7][7] = "R"  # Нижній правий

# Виведення шахівниці
for row in board:
    print(" ".join(row))
