numbers = [12, 5, 8, 3, 20, 1, 7]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены:", numbers)
