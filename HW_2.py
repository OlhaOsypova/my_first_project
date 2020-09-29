#вариант a-i-1
a = int(input('введите высоту треугольника:'))
n = 1
for i in range(a):
    print (' '*(a-i-1), '^'*n, ' '*(a-i-1))
    n += 2

