# Create an empty list called my_list
my_list=[]

# Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at the second position (index 1)
my_list.insert(1,15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50,60,70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of value 30
index_value_of_30= my_list.index(30)
print(f"The index vaulue of 30 on my list is {index_value_of_30}")

# Print the final list to verify all operations
print(f"The final list is: {my_list}")
