# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

a_tuple = ('asd', 'fgfd', 123, 45646, True, False)
my_dict = {}
for i in a_tuple:
    if type(i) in my_dict.keys():
        my_dict[type(i)].append(i)
    else:
        my_dict[type(i)] = [i]
print(my_dict)