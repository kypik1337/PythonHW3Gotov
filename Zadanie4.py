
COUNT = 2
my_list = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4, 7, 8, 9]

for item in set(my_list):
    if my_list.count(item) == COUNT:
        for _ in range(COUNT):
            my_list.remove(item)
print(sorted(my_list))





