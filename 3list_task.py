#find the largest number in the list
number=[2,3,7,4,5456,45,7,45,23,89,2346,27,783,6]
max=number[0]
for numbers in number:
    if numbers>max:
        max=numbers
print(max)