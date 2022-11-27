# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

number=int(input('Введите число: '))
list=[]
for i in range (1, number+1):
    list.append((1+1/i)**i)
for i in list:
    print(round(i, 3), end='; ')
# через print(list) выглядит слишком громоздко

sum=0
for el in list:
    sum+=el
print(f'\nсумма элементов равна {round(sum,3)}')