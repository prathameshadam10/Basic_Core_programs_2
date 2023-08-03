# 3. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[len(color_list)-1])
# 5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# import calendar
#
# def print_calendar(year, month):
#     # Create a TextCalendar object
#     cal = calendar.TextCalendar()
#
#     # Print the calendar for the given month and year
#     print(cal.formatmonth(year, month))
#
# def main():
#     try:
#         # Take input for year and month
#         year = int(input("Enter the year: "))
#         month = int(input("Enter the month: "))
#
#         # Check if the entered month is within the valid range (1 to 12)
#         if 1 <= month <= 12:
#             # Call the function to print the calendar
#             print_calendar(year, month)
#         else:
#             print("Invalid month! Please enter a month between 1 and 12.")
#     except ValueError:
#         print("Invalid input! Please enter valid numbers for year and month.")
#
# if __name__ == "__main__":
#     main()
# 7. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# list1 = [1, 5, 8, 3]
# is_present = 0
# x = int(input("Enter a number "))
# for i in list1:
#     if i == x:
#         is_present = True
#     else:
#         is_present = False
#
# print(is_present)
# 9. Write a Python program to concatenate all elements in a list into a string and return it.
def concatenate_list_elements(input_list):
    # Using the join() method to concatenate list elements into a string

    concatenated_string = ''.join(str(element) for element in input_list)

    return concatenated_string

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = concatenate_list_elements(my_list)
print(result)  # Output: "12345"
