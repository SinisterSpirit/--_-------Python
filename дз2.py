'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть.
'''
n = int(input("введите число монет: "))
print("0 - решка, 1 - орёл ")
zer = 0
one = 0
for i in range (n):
	c = int(input("введите 0 или 1"))
	if c == 0:
		zer = zer + 1
	if c == 1:
		one = one + 1
if one < zer:
	print("минимальное число монеток, которые нужно перевернуть: ",one)
else:
	print("минимальное число монеток, которые нужно перевернуть: ",zer)

'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

a = int(input("загадайте 2 числа от одного до 1000 и введите их сумму: "))
b = int(input("также введите их произведение: "))


'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
'''

n = int(input("введите число больше нуля: "))
print("степени числа 2:")
print("1")
m = 2
while m < n:
	print(m)
	m = m * 2
