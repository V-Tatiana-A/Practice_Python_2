# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# если список надо задать:
# string=input('Введите числа через пробел: ').split()
# array=list(map(int, string))
# print(array)
# ниже версия с рандомными числами

from random import randint as rnd
from random import sample as rnd_some

length=int(input('Введите размер списка: '))
array=[]
for i in range (length):
    array.append(rnd(0,100))
print(array)

# быстрое решение через random
print('Перемешали 1 способом:')
print(rnd_some(array, len(array)))

# через randint
def my_shuffle(list):
    result=[]
    while len(result)!=len(list):
        ind = rnd(0, len(list)-1)
        if list[ind] not in result:
            result.append(list[ind])
    return result

print('Перемешали 2 способом:')
print(my_shuffle(array))


