num = 1221
temp = num
reverse = 0
while num>0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print(reverse)
if temp == reverse:
    print("Pallindrome")
else:
    print("Not Pallindrome")