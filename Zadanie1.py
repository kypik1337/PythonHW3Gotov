my_list = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 7, 8, 9]
my_new_list = print(list(set(my_list))) #  сделали множество через функцию сет(убрали повторяющиеся значения)

new_list_morroy = []
for i in my_list:
    if i not in new_list_morroy:
        new_list_morroy.append(i)
        print(f'Добавляем элемент:= {i} в новый список :3')
    else:
        print(f'Число:= {i} есть в списке')
print(new_list_morroy)



