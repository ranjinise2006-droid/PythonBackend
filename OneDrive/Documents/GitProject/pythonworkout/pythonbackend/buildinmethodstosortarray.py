arr = [98, 67, 34, 12, 10, 99, 45]
print("before sorting:", arr)

# Method 1: sorted() returns a new sorted list.
print("using sorted():", sorted(arr))

# Method 2: sort() sorts the existing list in ascending order.
ascending_arr = arr.copy()
ascending_arr.sort()
print("using list.sort():", ascending_arr)

# Method 3: sorted() with reverse=True sorts in descending order.
print("using sorted(reverse=True):", sorted(arr, reverse=True))