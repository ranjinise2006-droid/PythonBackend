# Linear Search in Python

arr = [12, 45, 7, 23, 9, 54, 31]
search_value = 23

found = False

for i in range(len(arr)):
    if arr[i] == search_value:
        print(f"Element {search_value} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {search_value} not found in the array")
