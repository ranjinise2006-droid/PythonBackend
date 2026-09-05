a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
'''
# using if 
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print("The largest number is:", largest)
'''
# using if-elif-else statement:
'''
num1 = a
num2 = b
num3 = c
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)
'''

largest = max(a, b, c)
print("The largest number is:", largest)

