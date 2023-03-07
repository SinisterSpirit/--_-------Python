"""
Задача 22
"""

mas1 = [int(i) for i in input("введите первый набор чисел через пробел: ").split()]
mas2 = [int(i) for i in input("введите второй набор чисел через пробел: ").split()]
mas3 = []
c = 0

print(mas1)
print(mas2)

for i in range (len(mas1)):
	for j in range (len(mas2)):
		if mas1[i] == mas2 [j]:
			if len(mas2) > 0:
				for x in range(len(mas3)):
					if mas1[i] == mas3[x]:
						c = c+1
				if c == 0:
					mas3.append(mas1[i])
				else:
					c = 0
			else:
				mas3.append(mas1[i])

mas3.sort()

print(mas3)

"""
Задача 24
"""


mas1 = [int(i) for i in input("введите количество ягод на кустах через пробел через пробел: ").split()]
results = []

print(mas1)

for i in range (len(mas1)):
	if i == 0:
		c = mas1[i] + mas1[len(mas1)-1] + mas1[i+1]
		results.append(c)
	elif i == len(mas1)-1:
		c = mas1[i] + mas1[i-1] + mas1[0]
		results.append(c)
	else:
		c = mas1[i] + mas1[i-1] + mas1[i+1]
		results.append(c)

results.sort()

print(results[len(results)-1])
