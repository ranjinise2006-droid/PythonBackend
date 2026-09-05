num=123457
evenCount = 0
oddCount = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
    num //= 10
print("Number of even digits:", evenCount)
print("Number of odd digits:", oddCount)