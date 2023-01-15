# Сортировка выбором
my_list = [4, 6, 5, 11, 0, 9]

for i in range(0, len(my_list) -1):
    min_value = i
    for j in range(i+1, len(my_list)):
        if my_list[j] < my_list[min_value]:
            min_value = j
    my_list[i], my_list[min_value] = my_list[min_value], my_list[i]
print(my_list)
# Сортировка пузырьком
my_list = [4, 6, 5, 11,-1, 0, 9]
for i in range(len(my_list) -1):
    for j in range(len(my_list) -i -1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)