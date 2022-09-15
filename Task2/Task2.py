#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def MultiplicationOfNumbers(N):
    a = 1
    n = 1
    newlist = []
    
    while a <= N:
        n = a * n
        newlist.append(n)
        a += 1
    
    return(newlist)

number = int(input('Введите число: '))          #не работет с отрицательными числами (пока что)

print(f'Набор произведений чисел от 1 до {number}: {MultiplicationOfNumbers(number)}')