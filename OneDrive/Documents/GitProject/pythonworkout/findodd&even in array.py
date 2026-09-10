num = [3,2,8,6,90,87,45,13,12,11]
odd = []
even = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("The odd numbers in the array are:", odd)
print("The even numbers in the array are:", even)