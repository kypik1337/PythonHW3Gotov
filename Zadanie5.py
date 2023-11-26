
my_list = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 7, 8, 9]
new_list = []
new_my_list_por = []
new_my_list_zna = []

for nn, item in enumerate(my_list, 1):
    if item % 2 != 0:
        new_list.append(nn)
print(f'{new_list = }')

for item in enumerate(my_list, 1):
    new_my_list_por.append(item[0])
    new_my_list_zna.append(item[1])
print(new_my_list_por)
print(new_my_list_zna)


