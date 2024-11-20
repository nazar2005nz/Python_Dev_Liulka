import math


def gaussian_function(x, a=1, b=1, c=0):
    
    return a * math.exp(-b * (x - c) ** 2)


try:
    x = float(input("Введіть значення x: "))
    a = float(input("Введіть значення a (за замовчуванням 1): ") or 1)
    b = float(input("Введіть значення b (за замовчуванням 1): ") or 1)
    c = float(input("Введіть значення c (за замовчуванням 0): ") or 0)

    result = gaussian_function(x, a, b, c)
    print(f"Значення функції Гауса для x={x}, a={a}, b={b}, c={c}: {result}")

except ValueError:
    print("Будь ласка, введіть коректні числові значення!")

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")

total_apples = john + mary + adam

print("Загальна кількість яблук:", total_apples)

miles = 7.38
kilometers = 12.25

mile_to_kilometer = 1.61

miles_to_km = miles * mile_to_kilometer

km_to_miles = kilometers / mile_to_kilometer

print(miles, "miles is", round(miles_to_km, 2), "kilometers")
print(kilometers, "kilometers is", round(km_to_miles, 2), "miles")

x = float(input("Введіть значення x: "))


y = 3 * x**2 - 2 * x**2 + 3**x - 1

print("y =", y)

time_in_hours = 2
print("Hours:", time_in_hours)

a = 5
b = 2

addition = a + b

subtraction = a - b

multiplication = a * b

division = a / b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

x = float(input("Введіть значення x: "))

part1 = 1 / x
part2 = 1 / (x + 1)
part3 = part2 * (x + 1) / x
part4 = 1 / (x + part1 + part3)

y = part4

print("y =", y)

start_hour = int(input("Введіть годину початку (0-23): "))
start_minute = int(input("Введіть хвилини початку (0-59): "))
duration = int(input("Введіть тривалість у хвилинах: "))


total_minutes = start_hour * 60 + start_minute + duration
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(f"Час завершення: {end_hour}:{end_minute}")



