my_list = [8, 15, 4, 2]


def swap(input_list, index_1, index_2):
    # Using temp so we don't lose the original value at index_1
    temp = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = temp
    return input_list  # Make sure to return the swapped list

# The lowest index before we begin the for loop is 0


lowest_index = 0

for i in range(len(my_list)):
    if my_list[i] < my_list[lowest_index]:
        lowest_index = i

my_list = swap(my_list, lowest_index, 0)
print(my_list)
