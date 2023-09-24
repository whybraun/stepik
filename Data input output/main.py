print('Здравствуй, мир!')

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

print('*')
print('**')
print('***')
print('****')
print('*****')
print('******')
print('*******')

a = str(input())
print('Привет,', a)

a = str(input())
print(a, '- чемпион!')

a = str(input())
b = str(input())
c = str(input())
print(a)
print(b)
print(c)

a = str(input())
b = str(input())
c = str(input())
print(c)
print(b)
print(a)

print('I', 'like', 'Python', sep='***')

a = str(input())
b = str(input())
c = str(input())
d = str(input())
print(b, c, d, sep=a)

a = str(input())
print('Привет,', a, end='!')

a = int(input())
print(a)
print(a + 1)
print(a + 2)

a = int(input())
b = int(input())
c = int(input())

print(a + b + c)

a = int(input())
print('Объем =', a ** 3)
print('Площадь полной поверхности =', 6 * a ** 2)

a = int(input())
b = int(input())

print(3 * ((a + b) ** 3) + 275 * b ** 2 - 127 * a - 41)

a = int(input())
print('Следующее за числом', a, 'число:', a + 1)
print('Для числа', a, 'предыдущее число:', a - 1)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a + b + c + d) * 3)

a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

a1 = int(input())
d = int(input())
n = int(input())

an = a1 + d * (n - 1)

print(an)

x = int(input())
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')

b1 = int(input())
q = int(input())
n = int(input())

bn = b1 * (q ** (n - 1))

print(bn)

a = int(input())
print(a // 100)

n = int(input())
k = int(input())
print(k // n)
print(k % n)

n = int(input())
print((n + 1) // 2)

n = int(input())
print(n % 4)

a = int(input())

b = (a - 1) // 4 + 1

print(b)

a = int(input())
print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')

num = int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10

print('Сумма цифр =', a + b + c)
print('Произведение цифр =', a * b * c)

num = int(input())

a = num // 100
b = (num % 100) // 10
c = num % 10

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')

number = int(input())
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10
print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")

a = 4
b = 17

print('*' * b)

for i in range(a - 2):
    print('*' + ' ' * (b - 2) + '*')

print('*' * b)

a = int(input())
b = int(input())

print('Квадрат суммы', a, 'и', b, 'равен', (a + b) ** 2)
print('Сумма квадратов', a, 'и', b, 'равна', (a ** 2) + (b ** 2))

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a ** b) + (c ** d))

n = int(input())
n_sum = n + int(str(n) * 2) + int(str(n) * 3)
print(n_sum)