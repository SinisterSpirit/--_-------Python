### Задача 30 

a1= int(input("Введите значение 1-го элемента: "))
d=int(input("Введите разность элементов: "))
n=int(input("Введите количество элементов: "))
res = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*res)

### Задача 32

mass = [int(i) for i in input("введите набор чисел через пробел: ").split()]
res = []
minch = int(input("введите минимальное число: "))
maxch = int(input("введите максимальное число: "))
for i in range(len(mass)):
    if minch <= mass[i] <= maxch :
    	res.append(i)
print(res)