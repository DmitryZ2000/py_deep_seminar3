# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

# my_str = input('\nВведите строку: \n')
my_str = 'Однажды в студеную зимнюю пору я из лесу вышел был сильный мороз'
LETTER = 'ю'
print(f'\nПовторение буквы {LETTER} =  {my_str.count(LETTER)}\n')

my_new_str = my_str.split()
my_str = ''.join(my_new_str)
# print(my_str)
my_dic = {}
for i in range(len(my_str)):
    count = 1
    for j in range(i+1,len(my_str)):
        if my_str[i] == my_str[j]:
            count +=1
    if my_str[i] not in my_dic.keys():
        my_dic[my_str[i]] = count

print(my_dic)
