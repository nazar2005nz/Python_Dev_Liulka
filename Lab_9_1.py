def mysplit(string):
    # Перевіряємо, чи рядок не порожній
    if string.strip() == "":
        return []
    # Розділяємо рядок за пробілами
    return string.split()

# Тестуємо функцію
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(""))
print(mysplit("abc"))
print(mysplit("   "))

digits = [
    " ### \n#   #\n#   #\n#   #\n ### ",  # 0
    "  #  \n ##  \n  #  \n  #  \n ### ",  # 1
    " ### \n    #\n ### \n#    \n ### ",  # 2
    " ### \n    #\n ### \n    #\n ### ",  # 3
    "#   #\n#   #\n ### \n    #\n    #",  # 4
    " ### \n#    \n ### \n    #\n ### ",  # 5
    " ### \n#    \n ### \n#   #\n ### ",  # 6
    " ### \n    #\n   # \n  #  \n #   ",  # 7
    " ### \n#   #\n ### \n#   #\n ### ",  # 8
    " ### \n#   #\n ### \n    #\n ### "   # 9
]

def display_number(number):
    # Розбиваємо число на цифри
    rows = [""] * 5
    for digit in str(number):
        digit_representation = digits[int(digit)].split("\n")
        for i in range(5):
            rows[i] += digit_representation[i] + "  "
    return "\n".join(rows)

# Тестуємо
print(display_number(123))

def caesar_cipher(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + 1
            if char == 'Z':
                shifted = ord('A')
            elif char == 'z':
                shifted = ord('a')
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message

# Тестуємо
message = input("Enter your message: ").upper()
print(caesar_cipher(message))

def caesar_decipher(cryptogram):
    decrypted_message = ""
    for char in cryptogram:
        if char.isalpha():
            shifted = ord(char) - 1
            if char == 'A':
                shifted = ord('Z')
            elif char == 'a':
                shifted = ord('z')
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message

# Тестуємо
cryptogram = input("Enter your cryptogram: ").upper()
print(caesar_decipher(cryptogram))


def enhanced_caesar_cipher(message, shift):
    while not (1 <= shift <= 25):  # Перевіряємо, щоб зсув був у правильному діапазоні
        shift = int(input("Enter a valid shift (1-25): "))

    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            encrypted_message += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_message += char
    return encrypted_message


# Тестуємо
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
print(enhanced_caesar_cipher(message, shift))


