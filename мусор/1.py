def calculate_balance(day):
    if day == 0:
        return 0
    elif day % 3 == 0:
        return 500 * (day // 3)
    else:
        return 500 * ((day // 3) + 1)

# Тестируем функцию
for day in range(11):
    print(f"День {day} - {calculate_balance(day)} рублей")
