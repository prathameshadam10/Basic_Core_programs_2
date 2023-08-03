# Default function to implement conditions to check leap year

def checkLeap(year):
    '''
    Check the year is leap year
    :param year:int
    :return: none
    '''
    if ((year % 400 == 0) or
            (year % 100 != 0) and
            (year % 4 == 0)):
        print("Given year is Leap year ")

    else:
        print("Given year is Not Leap year ")



if __name__ == '__main__':
    year = int(input("Enter the number: "))
    checkLeap(year)
