arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 9, 5]

if len(arr1) != len(arr2):
    are_equal = False
else:
    are_equal = True
    for index in range(len(arr1)):
        if arr1[index] != arr2[index]:
            are_equal = False
            break

if are_equal:
    print("the arrays are equal")
else:
    print("the arrays are not equal")

        
''' are_equal = arr1 == arr2
# print("Are the arrays equal?", are_equal)

'''

        
        














