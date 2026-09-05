num = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    next_number = n1 + n2
    print(next_number, end=" ")
    n1 = n2
    n2 = next_number
