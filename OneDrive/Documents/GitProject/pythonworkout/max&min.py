arr = [2, 3, 6, 5, 9, 4]

max_value = arr[0]
min_value = arr[0]

for num in arr[1:]:
	if num > max_value:
		max_value = num
	if num < min_value:
		min_value = num

print("Maximum:", max_value)
print("Minimum:", min_value)