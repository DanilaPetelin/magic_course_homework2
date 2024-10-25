# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)

def do_simple(c1, c2):
    c1 = c1 if c1 >= 0 else -1 * c1
    for i in range(c1, 0, -1):
        if c1 % i == 0 and c2 % i == 0:
            return i
    return 1


def get_sum_fraction_number(a, b):
    a = list(map(int, a.split("/")))
    b = list(map(int, b.split("/")))

    c = [a[0] * b[1] + a[1] * b[0], a[1] * b[1]]
    c0 = c[0] // c[1]
    c1 = c[0] - c0 * c[1]
    c2 = c[1]

    i = do_simple(c1, c2)
    c1 = c1 // i
    c2 = c2 // i
    return c0, c1, c2


a = '1/3'
b = '4/4'

c0, c1, c2 = get_sum_fraction_number(a, b)
d0 = f"{a}+{b}= "
d1 = f"{c0 if c0 != 0 else ''} "
d2 = f"{c1}/{c2}" if c1 != 0 else ''

print(d0 + d1 + d2)