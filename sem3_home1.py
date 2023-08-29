# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [3,3,4,6,6,6,1,5,10,45,45,19,19,19]
clear_list = list(set(my_list))

multi_list = []
for i in clear_list:
  if my_list.count(i) > 1:
    multi_list.append(i)
print(f'\n{multi_list = }')