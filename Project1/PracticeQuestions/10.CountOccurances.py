# Count occurrences
# using loop
list = [1, 3, 3, 3, 7, 8, 9]
count = 0
x = 3
for i in list:
    if i == x:
        count += 1
print(count)

# count() function
list2 = [1, 2, 3, 3, 2, 8, 2]
print(list2.count(8))
