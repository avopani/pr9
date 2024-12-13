numbers = [1, 3, 2, 5, 4, 6, 8]

result = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        result.append(numbers[i])

print("Элементы, которые больше предыдущего элемента:", result)
