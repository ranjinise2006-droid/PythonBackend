arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in arr if x % 2 != 0]
even_numbers = [x for x in arr if x % 2 == 0]
print("Odd numbers in the array:", odd_numbers)
print("Even numbers in the array:", even_numbers)
