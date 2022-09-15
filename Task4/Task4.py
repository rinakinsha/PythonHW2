#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint        #randint - генератор случайного целого числа

n = int(input('Введите число: '))

listnum = []
for i in range(n):
    listnum.append(randint(-n, n))
print(listnum)

f = open('file.txt', 'w') # w - открытие файла на запись, содержимое файла удаляется, е. не существует - создается новый
while True:
    m = input('Укажите позицию для поиска произведения (начиная с 0): ')
    if m == "":              # условие выхода из цикла
        break
    f.write(m + "\n")
f.close()

multiply = 1
f = open('file.txt', 'r') # r - открытие файла на чтение
for i in f:
    if i == "":
        break
    multiply *= listnum[int(i)]
f.close()
print(multiply)