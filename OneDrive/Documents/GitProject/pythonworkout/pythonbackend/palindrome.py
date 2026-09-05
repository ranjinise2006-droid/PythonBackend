num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if original == rev:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is not a palindrome number.")
