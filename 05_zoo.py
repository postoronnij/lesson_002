#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код

zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код

k1, k2, k3, k4, k5, k6, k7 = zoo
lion = zoo.index(k1) + 1
lark = zoo.index(k7) + 1
print('Лев сидит в клетке номер ', lion)
print('Жаворонок сидит в клетке номер ', lark)
