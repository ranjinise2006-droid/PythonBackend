# Binary Search in Python

arr = [2, 4, 7, 10, 13, 18, 22, 27, 31, 35]
search_value = 18

start = 0
end = len(arr) - 1
found = False

while start <= end:
    mid = (start + end) // 2

    if arr[mid] == search_value:
        print(f"Element {search_value} found at index {mid}")
        found = True
        break
    elif arr[mid] < search_value:
        start = mid + 1
    else:
        end = mid - 1

if not found:
    print(f"Element {search_value} not found in the array")
