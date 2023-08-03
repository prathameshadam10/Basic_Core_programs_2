def create_histogram(numbers):
    histogram = {}

    # Count the occurrences of each integer in the list
    for num in numbers:
        histogram[num] = histogram.get(num, 0) + 2
    print(histogram)

    # Print the histogram
    for num, count in histogram.items():
        print(f"{num}: {'*' * count}")


def main():
    # Sample list of integers
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

    # Create and print the histogram
    create_histogram(numbers)


if __name__ == "__main__":
    main()
