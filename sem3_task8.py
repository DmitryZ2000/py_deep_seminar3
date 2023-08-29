# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

print()

dic_friends = {"Вася": ("рюкзак", "веревка", "фонарик","топор"), "Петя": ("рюкзак", "веревка", "консервы", "топор"),\
                "Сергей": ("рюкзак", "нож", "палатка"), "Игорь":("рюкзак", "веревка","вода","гречка","чай","спички")}

for key, value in dic_friends.items():
    print(key, 'взял', *value)   # Вещи взятые друзьями

friend_names = []
for key in dic_friends.keys():
    friend_names.append(key)

intersection_goods = set(dic_friends[friend_names[0]]) # Первый элемент из словаря

for i in range(1, len(friend_names)):
    intersection_goods = intersection_goods & set(dic_friends[friend_names[i]])

# print(f'\nУ каждого друга есть {intersection_goods}')
print('У каждого друга есть - ', *intersection_goods)

UNIQUE_FRIEND_NUMBER = 2  # Ищем уникальную вещь у друга № UNIQUE_FRIEND_NUMBER
friend_name = friend_names[UNIQUE_FRIEND_NUMBER]

unique_goods =  set(dic_friends[friend_name])

for key in dic_friends.keys():
    if key != friend_name:
        unique_goods = unique_goods - set(dic_friends[key])
# print(f'Только у {friend_name} есть {unique_goods}')
print('Только у', friend_name, 'есть -', *unique_goods)

friend_names.remove(friend_name) # Ищем пересечение у всех друзей кроме одного
intersection_goods = set(dic_friends[friend_names[0]]) # Первый элемент из словаря
for i in range(1, len(friend_names)):
    intersection_goods = intersection_goods & set(dic_friends[friend_names[i]])

diference_good = intersection_goods - set(dic_friends[friend_name])
# print(f'У {friend_name} отсутсвует {diference_good}')
print('У', friend_name, 'отсутсвует -', *diference_good)