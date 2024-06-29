# Check if an element exists in a list
element = (1, 46, 3, 6, 2, 1)
check_elem = int(input("Enter a number: "))

if check_elem in element:
    print(check_elem,"exist")
else:
    print("Element does not exist")

# Find if an element exists in the list using a loop
element2 = (1, 46, 3, 6, 2, 1)
check_elem = int(input("Enter a number: "))
for i in range(0, len(element2)):
    if check_elem in element:
        print(check_elem,"exist")

