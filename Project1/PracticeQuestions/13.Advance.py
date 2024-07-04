''''# Q.1
# How to count unique values inside a list

list = [2, 4, 4, 3, 3]
list2 = []
count = 0

for i in list:
    if i not in list2:
        count = count+1
        list2.append(i)

print(count)
'''
'''
# Q.2
# List product excluding duplicates

list = [1, 3, 5, 6, 3, 5, 1]
list2 = []
product = 1

for i in list:
    if i not in list2:
        list2.append(i)

for j in list2:
    product *= j
print(product)
'''
'''
# Q.3
#  Extract elements with Frequency greater than K
list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
list2 = []

def cal_frequency(list): # calculate frequency of unique elements
    dict = {}
    for i in list:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict


print(cal_frequency(list))

def frequency(k):
    for i in list:
        if list.count(i) >= k:
           # list.remove(i)
           # list.remove(i)
           # list.remove(i)
            print(i, end = " ")

print(frequency(2))
'''
'''
# Q.4
#  Test if List contains elements in Range
list = [23,44,3,12,90,100,12,33,12]

lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

for i in range(0,len(list)):
    if i >= lower_range and i <= upper_range:
        print("List elements are in range..")
        break
    else:
        print("List elements are not in range..")
        break
'''
'''
# Q.5
# Python program to check if the list contains three consecutive common numbers in Python

list = [4, 4, 4, 6, 6, 6]


for i in range(0,len(list)-2):
    index = 0
    if list[i] == list[i+1] and list[i+1] == list[i+2]:
            print(list[i], end = ",")
'''
'''
# Q.6
# program to find the Strongest Neighbour

list = [1, 2, 2, 3, 4, 5]
list2 = []
for i in range(1 ,len(list)):
    list2 = max(list[i], list[i-1])
    print(list2,end=" ")
'''
'''
# Q.7
# Program to print all Possible Combinations from the three Digits/ 4 digits
list = [0,1,0,1]

for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if i!=j and i!=k and i!=l and j!=k and j!=l and l!=k:
                    print(list[i], list[j], list[k], list[l])
'''
'''
# Q.8
# program to find all the Combinations in the list with the given condition
from itertools import combinations

list1 = ["Hello",23,"sonata", 90, [43,334]]
temp = combinations(list1,5)
index = 0
for i in list(temp):
    index += 1
    print("Combination: ", index, ": ", i)
'''
'''
# Q.9
# program to get all unique combinations of two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        list3.append({list2[j], list1[i]})

print(list3)
'''
'''
# Q. 10
# remove all the occurrences of an element from a list in Python
list = [1, 1, 2, 4, 6, 7, 7, 9, 9]

remove_elem = int(input("Enter the elem to remove: "))

while remove_elem in list:
    list.remove(remove_elem)
    
print(list)
'''
'''
# Q. 11
# – Remove Consecutive K element records
list = [(1, 1, 2, 3), (5, 6, 6, 9), (5, 5, 8, 6), (6, 6, 7, 8)]
print(list)
list2 = []
K = int(input("Enter the: "))
for i in list:
    flag = False
    for j in range(len(i)-1):
        if i[j] == K and i[j+1] == K:
            flag = True
            break
    if not flag:
        list2.append(i)

print(list2)
'''



