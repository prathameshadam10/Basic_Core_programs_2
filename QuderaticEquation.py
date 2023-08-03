def quadratic_equation(p, q, r):
    """
    
    :param p: int
    :param q: int
    :param r: int
    :return: None
    """
    delta = (q * q) - (4 * p * r)

    first_root = (-q + delta ** 2) / (2 * p)
    print("Value of first root :" + str(first_root))
    second_root = (-q - delta ** 2) / (2 * p)
    print("Value of second Root :" + str(second_root))


if __name__ == '__main__':
    a = int(input("Enter Value of a :"))
    b = int(input("Enter Value of b :"))
    c = int(input("Enter Value of c :"))

    quadratic_equation(a, b, c)


