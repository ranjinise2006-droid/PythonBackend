name = input("Enter a name: ")
'''
rev = name[::-1]
print("Reversed name:", rev)
'''

'''
rev2 = "".join(reversed(name))
print("Reversed name:", rev2)
'''

# using for loop
'''
rev3 = ""

for char in name:              
   rev3 = char + rev3
print("Reversed name:", rev3)
'''

# using while loop
rev4 = ""
i = len(name) - 1
while i >= 0:
    rev4 = rev4 + name[i]
    i -= 1
print("Reversed name:", rev4)