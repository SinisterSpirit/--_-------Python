# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input("введите трёх значное число: "))

c = a % 10 + a//10 % 10 + a//100 % 10

print("сумма цифр в введённом числе: ",c)

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
журавликов, чем Петя и Сережа вместе?
'''

s = int(input("введите количество журавликов: "))

petya = s/4
sergei = s/4
katya = s/2

print("Петя: ",petya,"Катя: ",katya,"Серёжа: ",sergei)

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
'''
a = int(input("введите номер билета: ")) 

fh = a % 10 + a//10 % 10 + a//100 % 10
a = a//1000
sh = a % 10 + a//10 % 10 + a//100 % 10

if fh == sh :
	print("билет счастливый")
else:
	print("билет не счастливый")

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
'''
n = int(input("введите количество долек в длинну: "))
m =  int(input("введите количество долек в ширену: "))
k = int(input("введите количество долек которые необходимо отломить: "))
if k <= 0:	
	if k > n*m:
		print("в шоколадки столько нет")
	elif k == n*m:
		print("ешь всю")
	else:
		if k % n == 0 or k % m == 0:
			print("у тебя всё получится")
		else:
			print("за раз столько не отломить")
else:
	print("правильно у нас диета")