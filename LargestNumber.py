def find_largest_number(first_number, second_number, third_number):
    '''

    :param first_number: int
    :param second_number: int
    :param third_number: int
    :return: None
    '''
    if first_number > second_number and first_number > third_number:
        print(str(first_number) + " is Greater")
    elif second_number > first_number and second_number > third_number:
        print(str(second_number) + "is Greater")
    else:
        print(str(third_number) + "is Greater")


if __name__ == '__main__':
    first_number = int(input("Enter First Number : "))
    second_number = int(input("Enter  second Number : "))
    third_number = int(input("Enter  third Number : "))
    find_largest_number(first_number, second_number, third_number)
