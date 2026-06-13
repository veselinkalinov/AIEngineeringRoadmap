my_list = [4, 8, 2, 15]


def swap(input_list, index_1, index_2):
    input_list[index_1], input_list[index_2] = input_list[index_2], input_list[index_1]
    return input_list


for i in range(len(my_list)):
    lowest_index = i
    for j in range(i, len(my_list)):
        if my_list[j] < my_list[lowest_index]:
            my_list = swap(my_list, j, i)
            break

print(my_list)
