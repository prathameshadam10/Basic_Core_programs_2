import random


def flip_coin(num_of_flips):
    heads = 0
    tails = 0
    for i in range(num_of_flips):
        coin = random.randint(0, 1)
        if coin < 0.5:
            tails += 1
        else:
            heads += 1
    percent_head = (heads / num_of_flips) * 100
    percent_tail = (tails / num_of_flips) * 100
    print("Percentage Of head " + str(percent_head))
    print("Percentage Of Tail " + str(percent_tail))


if __name__ == '__main__':
    x = input("Enter the Num of times Flips coin ")
    flip_coin(int(x))
