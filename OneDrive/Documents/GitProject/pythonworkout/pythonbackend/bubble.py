arr = [2, 3, 7, 5, 8, 1, 9]

print("array before sorting:", arr)

n = len(arr)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("after array sorting:", arr)
