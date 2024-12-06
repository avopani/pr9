''' Пользователь вводит числа a и b. Создать список, содержащий
квадраты целых чисел расположенных между ними.'''

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 
    
while True:
    a = input('Введите целое число a: ')    
    b = input('Введите целое число b: ')
    if is_number(a) and is_number(b):
        a = int(a)
        b = int(b)
        niz = min(a,b)    
        verh = max(a,b)
        list = [(number)*(number) for number in range(niz+1,verh)]
        print(list)
        break
    else:
        print('Вы неправильно ввели целые числа')
        
