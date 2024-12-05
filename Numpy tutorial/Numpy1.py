import numpy as np

np1 = np.array([1, 2, 3])
print(np1)
print(np1.shape)
#Range
np2 = np.arange(10)
print(np2)

# Step
np3 = np.arange(0,10,2)
print(np3)

# zeros

np4 = np.zeros(10)
print(np4)

#multi dimensional zeros

np5 = np.zeros((2,10))
print(np5)

# Full

np6 = np.full((10), 6)
print(np6)

# multi full
np7 = np.full((2,10), 7)
print(np7)

# python list to np

list1 = [1,2,3,4,5,6,7,8,9]
np8 = np.array(list1)
print(np8[8])