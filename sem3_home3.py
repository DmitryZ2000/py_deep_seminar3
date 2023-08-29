# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

CAPACITY = 20

dic_equipment = {'rope': 10, 'lamp': 1, 'map' : 1, 'battary_pack': 3, \
                 'tent': 4, 'cloths': 4, 'fins': 2, 'glasses': 1, 'match': 0.5}

pack_list = []
weight = 0
for key, value in dic_equipment.items():
    if weight + value < CAPACITY:
        pack_list.append(key)
        weight +=value

print(pack_list, weight)

#Для того чтобы перебрать все варианты, надо проработать по всем биномиальный коэффициентам