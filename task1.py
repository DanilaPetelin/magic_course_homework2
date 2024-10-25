# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



def find_position_str_in_list_1(str_list, f_str, num):
    count, l_i = 0, len(f_str)
    for i in range(len(str_list)):
        s_index, pos = 0, 0
        while True:
            pos = str_list[i].find(f_str, s_index)
            if pos == -1 or count == num:
                break
            count += 1
            s_index = pos + l_i
        if count == num:
            return i
    return -1

def find_position_str_in_list_2(str_list, f_str, num):
    count = 0
    for i in range(len(str_list)):
        if str_list[i] == f_str:
            count += 1
        if count == num:
            return i
    return -1

"""
find_position_str_in_list_1 не совсем по условиям сначала делал
    тут проверяю на вхождение искомой строки в качестве подстроки в элементе списка

find_position_str_in_list_2 уже по условиям задачи
"""
num =2
str_list= ["qwe", "asd", "zxc", "qwerty", "qwe", "qweertqwe"]
f_str = "qwe"
i = find_position_str_in_list_2(str_list, f_str, num)
print(f"ответ {i}")
