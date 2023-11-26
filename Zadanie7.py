my_list = input('Add Stroka: ')
my_dict = {}

for char in set(my_list):
    my_dict[char] = my_list.count(char)
print(my_dict)

my_dict2 = {}
for char in my_list:
    if char not in my_dict2:
        my_dict2[char] = 1
    else:
        my_dict2[char] +=1
print(my_dict2)

my_dict3 = {}
for char in my_list:
    my_dict3[char] = my_dict3.get(char, 0 ) + 1
print(my_dict3)


