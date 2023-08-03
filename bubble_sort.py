def sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp




my_list = [5, 3, 8, 6, 7, 2]
sort(my_list)
print(my_list)

x = 10
y = int(0o1)
print(y)
