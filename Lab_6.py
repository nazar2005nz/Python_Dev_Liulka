def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

# Тестування
test_years = [1900, 2000, 2024, 2023]
expected_results = [False, True, True, False]

for year, expected in zip(test_years, expected_results):
    result = is_leap_year(year)
    print(f"Year {year}: {result} (Expected: {expected})")

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days[month - 1]

# Тестування
test_cases = [(2024, 2), (2023, 2), (2024, 1), (2023, 13)]
for year, month in test_cases:
    print(f"Year {year}, Month {month}: {days_in_month(year, month)}")

def day_of_year(year, month, day):
    if not (1 <= month <= 12) or day < 1:
        return None

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days[1] = 29

    if day > month_days[month - 1]:
        return None

    return sum(month_days[:month - 1]) + day

# Тестування
test_cases = [(2024, 3, 1), (2023, 2, 28), (2023, 2, 29), (2024, 12, 31)]
for year, month, day in test_cases:
    print(f"Year {year}, Month {month}, Day {day}: {day_of_year(year, month, day)}")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Тестування
for num in range(1, 21):
    if is_prime(num):
        print(num, end=" ")


        def liters_100km_to_miles_gallon(liters):
            miles_per_100km = 100 * 1000 / 1609.344
            gallons = liters / 3.785411784
            return miles_per_100km / gallons


        def miles_gallon_to_liters_100km(miles):
            kilometers_per_mile = 1609.344 / 1000
            liters_per_gallon = 3.785411784
            return (100 / (miles * kilometers_per_mile)) * liters_per_gallon


        # Тестування
        print(liters_100km_to_miles_gallon(3.9))
        print(miles_gallon_to_liters_100km(60.31143162393162))

def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Тестування
print(is_a_triangle(3, 4, 5))  # True
print(is_a_triangle(1, 10, 12))  # False

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

# Тестування
print(is_a_right_triangle(3, 4, 5))  # True
print(is_a_right_triangle(5, 12, 13))  # True
print(is_a_right_triangle(1, 2, 3))  # False

