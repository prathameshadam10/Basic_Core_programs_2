def check_even_odd(num):
    '''
    check weather given number is even or odd
    :param num: int
    :return: None
    '''
    if num % 2 == 0:
        print("Given Number is Even")
    else:
        print("Given Number is Odd")


if __name__ == '__main__':
    number = int(input("Enter a number :"))
    check_even_odd(number)
