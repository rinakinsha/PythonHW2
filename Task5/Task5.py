# Реализуйте алгоритм перемешивания списка

import random

newlist = [i for i in range(1,15)]
print(f'Сгенерированный список: {(newlist)}')

random.shuffle(newlist)                    # random.shuffel() - метод перемешиванния списка
print(f'Перемешанный список: {(newlist)}')