def find_quotient_reminder(p, q):
    '''

    :param p: int
    :param q: int
    :return: None
    '''
    quotient = p / q
    print("The Value Of Quotient :" + str(quotient))
    reminder = p % q
    print("The Value of Reminder :" + str(reminder))


if __name__ == '__main__':
    a = int(input("Enter Value of numerator "))
    b = int(input("Enter Value of Denomenator "))
    find_quotient_reminder(a, b)