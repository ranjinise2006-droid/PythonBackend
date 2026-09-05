original = input("Enter a number: ")
reversed_number = original[::-1]

if original == reversed_number:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is not a palindrome number.")