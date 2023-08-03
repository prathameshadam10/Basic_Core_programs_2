def find_harmonic_series(_num):
    result = 0.0

    while _num > 0:
        _num -= 1
        print(str(result) + " ")
    print("The Harmonic series " + str(result))


if __name__ == '__main__':
    num = int(input("Enter the number for harmonic value"))

    print("The Harmonic series.....")
    find_harmonic_series(num)
    
