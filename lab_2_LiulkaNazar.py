print("Programming***Essentials***in...", end="")
print("Python")
def draw_arrow():
    arrow = [
        "   *   ",
        "  * *  ",
        " *   * ",
        "***  ***",
          "*  *",
          "*  *",
          "*****"
    ]
    for line in arrow:
        print(line)

draw_arrow()
print("I'm student")
print("I`m\nlearning\nPython")
octal_number = "500"  # Вісімкове число як рядок
decimal_number = int(octal_number, 8)  # Переведення у десяткову систему
print(decimal_number)  # Виведення результату
hex_number = "777"
decimal_number = int(hex_number, 16)
print(decimal_number)





