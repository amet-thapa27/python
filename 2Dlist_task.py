#wap to remove the duplicates from the list
number=[1,4,6,8,5,3,2,1,3]
output=[]
for item in number:

    if item not in output:
        output.append(item)
output.sort()
print(output)
print(number)

set_2 = {1,2,3,3,4,5}
print(set_2)