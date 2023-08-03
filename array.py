def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


if __name__ == '__main__':
    array = [5, 2, 3, 4, 1, 6, 7]

    # Take sum as input from user
    summ = int(input("Enter the target "))

    # print array
    print("Array= ", array)

    #call function find
    find(array, len(array), summ)
