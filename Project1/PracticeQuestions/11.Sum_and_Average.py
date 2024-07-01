# Find sum and average of List in Python
# 11
'''
list = [2, 4, 5, 1, 9, 6, 3, 8]

#def sum():
 #   sum = 0
  #  for i in list:
   #     sum+=i
   # return sum

count = sum(list) # predefined function in python to calculate sum in list
def average():
    avg = sum(list) /len(list)
    return avg

print(count)
print(average())
'''

'''
# Q.12
# Python | Multiply all numbers in List
list = [2, 4, 3, 1, 4, 6, 7]
product = 1
for i in list:
    product *= i

print(product)
'''
'''
# Q. 13
# smallest and largest number in a list
list = [2, 4, 3, 1, 4, 6, 7]

def largest(list):
    list.sort()
    print(list[len(list)-1])

def smallest(list):
    list.sort()
    print(list[0])

largest(list)
smallest(list)

# using min() function
print(min(list))
print(max(list))
'''
'''
# Q. 14
# Find the second largest number in the list
list = [1,2,1,5,10,4,2,2,9]

list.sort()
print(list[-2])
'''
'''
# Q.15
# Print Even and Odd number and their count
list = [2, 5, 7, 9, 11, 12, 24, 35, 67, 80]
def even(list):
    count = 0
    for i in list:
        if i % 2 == 0:
            print(i)
            count += 1
    print(count)


def odd(list):
    count1 = 0
    for i in list:
        if i % 2 != 0:
            print(i)
            count1 += 1

    print(count1)


print("Even numbers" ,even(list))
print("Odd numbers" ,odd(list))
'''
'''
# Q. 16
# Remove positive and negative numbers in list and count the positive and negative numbers

list = [2, -5, 7, -9, 11, 12, 24, -35]

def remove_positive():
    count = 0
    for i in list:
        if i > 0:
            list.remove(i)
    for j in list:
        count += 1

    print(count)

def remove_negative():
    count = 0
    for i in list:
        if i < 0:
            list.remove(i)
    for j in list:
        count += 1

    print(count)

def count_positive_and_negative(): # count positive and negative integers
    pos_count = 0
    neg_count = 0
    for i in list:
        if i < 0:
            neg_count += 1
        elif i > 0:
            pos_count += 1
    print(pos_count, neg_count)

print(list)
count_positive_and_negative()
# remove_positive()
# print(list)
# remove_negative()
# print(list)
'''
'''
# Q.17
# Remove multiple elements from the list
list = [2, 7, 9, 11, 12, 24]
# using del function
# del list[0:4]
# print(list)

# loop and condition
for i in list:
    if i % 2 == 0:
        list.remove(i)


print(list)
'''
'''
# Q. 18
# Remove empty tuples from list

list = [(1,2,3),(), (5,6,7),(),(8,9,10)]

for i in list:
    if i == ():
        list.remove(i)


print(list)
'''

# Q.19
# Print duplicate elements of list to another list

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = []
list3 = []
for i in list:
    if i not in list2:
        list2.append(i)
    elif i not in list3:
        list3.append(i)
'''
 Execution
 list: [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
 
 Iteration 1:
 i = 10
 10 is not in list2, so 10 is appended to list2.
 list2 becomes [10]

 Iteration 2: 
 i = 20
 20 is not in list2, so 20 is appended to list2.
 list2 becomes [10, 20]

 Iteration 3:
 i = 30
 30 is not in list2, so 30 is appended to list2.
 list2 becomes [10, 20, 30]

 Iteration 4:
 i = 20
 20 is in list2 but not in list3, so 20 is appended to list3.
 list3 becomes [20]

 Iteration 5: 
 i = 20
 20 is in list2 and already in list3, so no action is taken.

 Iteration 6: 
 i = 30
 30 is in list2 but not in list3, so 30 is appended to list3.
 list3 becomes [20, 30]

 Iteration 7: 
 i = 40
 40 is not in list2, so 40 is appended to list2.
 list2 becomes [10, 20, 30, 40]

 Iteration 8: 
 i = 50
 50 is not in list2, so 50 is appended to list2.
 list2 becomes [10, 20, 30, 40, 50]

 Iteration 9: 
 i = -20
 -20 is not in list2, so -20 is appended to list2.
 list2 becomes [10, 20, 30, 40, 50, -20]

 Iteration 10: 
 i = 60
 60 is not in list2, so 60 is appended to list2.
 list2 becomes [10, 20, 30, 40, 50, -20, 60]

 Iteration 11: 
 i = 60
 60 is in list2 but not in list3, so 60 is appended to list3.
 list3 becomes [20, 30, 60]

 Iteration 12: 
 i = -20
 -20 is in list2 but not in list3, so -20 is appended to list3.
 list3 becomes [20, 30, 60, -20]

 Iteration 13: 
 i = -20
 -20 is in list2 and already in list3, so no action is taken.
  Final Output
 list3 now contains the duplicate elements [20, 30, 60, -20].
'''
print(list3)
