num = int(input("Enter a number: "))
'''
# Method 1: Using while loop
n = num
reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Method 1 - While loop:", reverse)


# Method 2: Using string slicing
reverse = int(str(num)[::-1])

print("Method 2 - String slicing:", reverse)


# Method 3: Using reversed()
reverse = int("".join(reversed(str(num))))

print("Method 3 - reversed():", reverse)

'''
#  Method 4: Using for loop
reverse = ""

for digit in str(num):
    reverse = digit + reverse

reverse = int(reverse)

print("Method 4 - For loop:", reverse)