# 2. Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# DUBL_POINT = 2
# my_list = [1,2,3,4,5,6,7,8,9,7,6,4,33,2,233,234]
# my_res = []
# print(f'Наш список в первоначальном виде:= {my_list}')
# for item in set(my_list):
#     if my_list.count(item)>=DUBL_POINT:
#         my_res.append(item)
# print(f'Итоговый и обработанный список:= {my_res}')

# 3. В большой текстовой строке подсчитать количество 
# встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или 
# из документации к языку.

# import re
# CHASTNOE_SLOVO = 10
# text_input = input('Введите вашу текстовую строку: ')
# text_input= text_input.lower()
# text_input = re.sub(r'[^\w\s]',' ', text_input)
# elements = text_input.split(' ')
# my_dir = []
# for item in set(elements):
#     my_dir.append((item, elements.count(item)))

# my_dir.sort(key=lambda a: a[1])
# my_dir.pop()
# my_dir.reverse()
# for i in range(CHASTNOE_SLOVO):
#     print(f'Слово и кол-во повторов:= {my_dir[i]}')

# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

volume= int(input('Количество всех вещей : '))
max_mass = int(input('Максимальная грузоподьемность : '))
backpack = dict()
def mass_chek():
    while True:
        mass = input("Введите массу: ")
        if not mass.isnumeric():
            print("Вы ввели не число. Попробуйте снова: ")
        else:
            mass=int(mass)
            break
    return mass

for i in range(volume):
        key = input('введите вещь: ')
        value =mass_chek()
    
        backpack[key] = value
count=0
for key, value in backpack.items():
    count = count + value
    if count<=max_mass:
        print(key)
    else:
        count = count - value

