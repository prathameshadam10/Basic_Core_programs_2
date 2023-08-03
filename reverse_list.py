


def reverse_list(my_list, start, end):
    while start < end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

my_list = [2, 43, 56, 4, 67, 89, 1, 34, 69]
reverse_list(my_list, 0, len(my_list)-1)
print(my_list)

input_list = [1, 2, 3, 4, 5, 6, 7, 8]
output_list = []
for i in range(len(input_list)-1, -1, -1):
    output_list.append(input_list[i])
print(output_list)
