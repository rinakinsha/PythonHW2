#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def Sum(n):
    sum = 0
    newlist = []
    for i in range(1, n + 1): 
        sum += ((1 + 1 / i)**i)
        newlist.append(round(((1 + 1 / i)**i), 1))
    print(f'Список: {newlist}')
    return (sum)

number = int(input('Введите число: '))

print(f'Сумма чисел: {round(Sum(number),1)}')