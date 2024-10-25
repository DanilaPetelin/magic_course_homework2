# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def get_summ_on_odd_positions(l_n):
    s=0
    for i in l_n[1::2]:
        s += i
    return s

l_n = [2,3,4,5,6,35,36,37]

print(get_summ_on_odd_positions(l_n))