import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]


user_numbers = []
for i in range(len(ticket)):
    number = int(input(f"Выберите число из строки {i + 1} (возможные числа: {ticket[i]}): "))
    while number not in ticket[i]:
        number = int(input(f"Неверный ввод. Пожалуйста, выберите число из строки {i + 1} (возможные числа: {ticket[i]}): "))
    user_numbers.append(number)

lottery_numbers = [random.choice(row) for row in ticket]

print("\nВаши числа:", user_numbers)
print("Случайно выбранные числа:", lottery_numbers)

matched_numbers = set(user_numbers) & set(lottery_numbers)
print("Совпавшие числа:", matched_numbers)
print("Количество совпадений:", len(matched_numbers))
