# Programs on List of Lists
import random
'''
# Q1 Remove empty list from lists

list = [[1,2],[],[3,4,5],[],[6,7,8,9]]
print(list)
for i in list:
    if i == []:
        list.remove(i)

print(list)
'''
'''
# Q.2 Convert List to List of dictionaries

test_list = ["Gojo", 8, "saturo", 11]
key_list = ["name", "id"]
list = []

for i in range(0,len(test_list),2):
    list.append( {key_list[0] : test_list[i], key_list[1]: test_list[i+1]})


print(list)
'''
'''
# Q.3 Convert Lists of List to Dictionary

test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
d = dict()
for i in test_list:
    d[tuple(i[:2])] = tuple(i[2:])

print(d)
'''
'''
# Q.4 Finding uncommon 2 lists
list1 = [[2, 2, 2], [2, 2, 1], [1, 1, 2], [1, 2, 1], [1, 1, 1]]
list2 = [[2, 2, 2], [2, 1, 1], [2, 1, 2], [1, 2, 1], [1, 1, 1]]

print(list1)
print(list2)

for i in list1:
   if i not in list2:
       print("List not in list2 ", i)

for j in list2:
    if j not in list1:
        print("List not in list1 ", j)
        
'''
'''
# Q.5 Program to select random value from lists of list

lists = [[11, [10, 9]], [12, 22, 21], [16, 17, 82], [52,53,54]]
row = [0,1,2]
# number = random.choice(lists[random.choice(row)])
# print(number)

sub = random.choice(lists)
print(sub)

num = random.choice(sub)
print(num)

N = random.choice(num)
print(N)
'''
'''
# Q.6 Program to reverse sort the lists of list
lists = [[11, 10, 9], [12, 22, 21], [16, 17, 82], [52, 53, 54]]
print(str(lists))
for i in lists:
    i.sort(reverse=True)

print(str(lists))
'''

# Q.7 Pair elements with Rear element in Matrix Row
'''
list = [[10, 9,4], [12, 22, 21], [16, 17,5]]
list2 = []
for i in list:
    temp = []
    for j in range(len(i)-1):
        temp.append([i[j],i[-1]])
    list2.append(temp)

print(list2)
'''

list23 = [[10, 9, 4], [12, 22]]

for i in list23:
    for j in range(len(i)-1):
        print(i[j])
