# Python program to interchange first and last elements in a list

list = [12, 35, 44, 9]

def swapList():
    # for i in range(0,len(list) - 1):
        temp = list[0]
        list[0] = list[len(list) - 1]
        list[len(list) - 1] = temp

print(list)
print(swapList())
print(list)

