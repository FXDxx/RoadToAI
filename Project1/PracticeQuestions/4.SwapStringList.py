# Python – Swap elements in String list

str_list = ["Apple", "Banana", "Cherry", "Strawberry", "Guava", "Pineapple"]

str_list = ", ".join(str_list)
str_list = str_list.replace("p", "_").replace("r", "p").replace("_", "r")
print(str_list)