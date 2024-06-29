# Different Ways to Remove from a List
# 1
list1 = [1,2,3,4,5,6,7,8]
print(list1)
list1.clear()
print(list1)
# 2
list2 = ["A","b","d","j"]
print(list2)
list2 = []
print(list2)

# 3
list3 = [10,20,30,40,50,60,70,80,90]
print(list3)
# list3*=0
del list3[0:4]
print(list3)

# 4
list4 = [1,2,3,4,5,6,7]
print(list4)
for i in range(0, len(list4)):
    if i != 0:
        list4.pop()
print(list4)