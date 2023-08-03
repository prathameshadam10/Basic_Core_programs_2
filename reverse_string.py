my_string = "hello"
x = len(my_string)
output_ = ""

for i in range(x - 1, -1, -1):
    output_ += my_string[i]
print(output_)

