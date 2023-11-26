

my_list = sorted(input('Введите строку текста: ').split())
max_long = 0


for item in my_list:
    if len(item) > max_long:
        max_long = len(item)
for nn, word in enumerate(my_list, 1):
    print(f'{nn}. {word:>{max_long}}')