arr = ["java", "python", "c", "php", "dsa", "python"]

seen = []
duplicates = []

for item in arr:
    if item in seen and item not in duplicates:
        duplicates.append(item)
    seen.append(item)

print("Original array:", arr)
print("Duplicate elements:", duplicates)
