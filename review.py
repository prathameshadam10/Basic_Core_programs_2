my_list = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(my_list)
# my_list2 = my_list[:length//2]
# my_list3 = my_list[length//2:]
# result = []
# for i in [my_list2, my_list3]:
#     result += [*i[2:], *i[:2]]
# print(result)

# output_array = [3, 4, 1, 2, 7, 8, 5, 6]

# print(my_list)
# temp1 = my_list[0]
# temp2 = my_list[1]
#
# my_list[0], my_list[1] = my_list[2], my_list[3]
# my_list[2], my_list[3] = temp1, temp2
# temp3 = my_list[4]
# temp4 = my_list[5]
# my_list[4], my_list[5] = my_list[6], my_list[7]
# my_list[6], my_list[7] = temp3, temp4
#
# print(my_list)
for i in range(len(my_list)//2):
   for j in range(len(my_list)//2):
       temp = my_list[i]
       my_list[i] = my_list[j]
       my_list[j] = temp
for i in range(4, len(my_list)):
    for j in range(4,len(my_list)):
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
#
#



print(my_list)

# print(my_list)
# a = 10
# b = 5
# a,b = b,a
#
# print(a,b)




