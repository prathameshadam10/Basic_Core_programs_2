# 2. Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
def main():


    # Take input from the user
    user_input = input("Enter a sequence of comma-separated numbers: ")
    print(user_input)

    # Split the input by commas and create a list
    number_list = user_input.split(',')
    print(number_list)
    #
    # Strip any leading/trailing spaces from each number in the list
    number_list = [number.strip() for number in number_list]
    print(number_list)
    #
    # Convert the list into a tuple
    number_tuple = tuple(number_list)
    print(number_tuple)

    # Print the list and tuple
    print("List:", number_list)
    print("Tuple:", number_tuple)

if __name__ == "__main__":
    main()

