# Python Program to Swap Two Elements in a List
list = [1,2,3,4,5,6,7,8,9]
def swapTwoElements(pos1, pos2):
    pos1 = int(input("Enter pos1: "))
    pos2 = int(input("Enter pos2: "))
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if i == pos1 and j == pos2:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

print(list)
print(swapTwoElements(1,5))
print(list)