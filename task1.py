# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number=input('Введите число: ')

print('Реешение через строку')
sum=0
num=number.replace('.', '')
for n in num:
    sum+=int(n)
print(sum)

print('Реешение через число')
sum2=0
num2=int(num)
while num2>0:
    sum2+=num2%10
    num2 = num2//10
print(sum2)
