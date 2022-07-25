#Вычислить результат деления двух чисел c заданной точностью d
#Пример:
# при d = 0.001, π = 3.141.
num1 = float(input('Введите число №1: '))
num2 = float(input('Введите число №2: '))
d = input('Введите точность после запятой: ')
division = num1 / num2

def accuracy(d):
    d = int(len(d[2:]))
    return d
    
if len(d) >= 3 and len(d) <= 12:
    print(round(division, accuracy(d)))
else:
    print('Некорректно введена точность.')