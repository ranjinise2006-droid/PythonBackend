arr = [1, 2, 3, 4, 6, 7]

sum = 0
for i in arr:
    sum += i

sum1 = 0
for i in range(1, len(arr) + 2):
    sum1 += i

missing_number = sum1 - sum

print(f"Sum of elements in array: {sum}")
print(f"Sum of expected range: {sum1}")
print(f"Missing number is: {missing_number}")

