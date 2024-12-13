numbers = [] 

while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    
    if user_input.lower() == 'end':  
        break
    
    try:
        number = int(user_input)  
        numbers.append(number)  
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")  

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
