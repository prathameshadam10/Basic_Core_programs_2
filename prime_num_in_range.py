def find_prime_num_in_range(start, end):
    primes = []
    count = 0
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            if i != 1:
                print(i, end=" ")


find_prime_num_in_range(5, 10)
