# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# my_str = input('\nВведите строку: \n')
my_str = 'Однажды в студеную зимнюю пору я из лесу вышел был сильный мороз'
my_list = my_str.split()
# for word in my_list:
#     print(word)

# print()

my_list.sort()
my_dic = {}
for word in enumerate(my_list,start=1):
    my_dic[word[0]] = word[1]

# print(my_dic)

max_value_len = 0
for value in my_dic.values():
    if max_value_len < len(value):
        max_value_len = len(value)

print(max_value_len)

# for key, value in my_dic.items():
#     print(f'{key: > max_value_len} {value}')  не удалось реализовать такую конструкцию

for key, value in my_dic.items():
    print(f'{key: > 8} {value}') 
