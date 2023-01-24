import numpy as np

# numpy is a library that simplifies array handling.

np.array([10, 20, 24, 5, 15, 50])

a = np.array([10, 20, 30, 40, 50, 60, 70])
print(a[4])

# Print from index 3
print(a[3:])

# Print from index 3 to prev index 5
print(a[3:5])

# Print every 3 positions
print(a[0::3])

# Create an array of 5 positions with the value 0
print(np.zeros(5))

# Bidimentional array of ones (#cols, #rows)
ones = np.ones((5, 3))
print(ones)

# Print the type of n dimensions array ones
print(type(ones))

# Print data type of an index
print(type(ones[2][2]))

# Equidistant line space
print(np.linspace(3, 10, 5))

# Array of 2 dimensions
b = [['x', 'y', 'z'], ['a', 'b', 'c']]
print(b)

# Count the number of dimensions
print(np.ndim(b))

# Sort the array
c = [33, 10, 2, 50, 42]
print(np.sort(c))

# List of users
headers = [('name', 'S10'), ('age', int)]
data = [('Juan', 10), ('Maria', 70), ('Javier', 42), ('Samuel', 15)]
users = np.array(data, dtype=headers)

print(np.sort(users, order="age"))

# Dynamically fills an array from 0 to 24
print(np.arange(25))

# Dynamically fills an array from 5 to 30
print(np.arange(5, 30))

# Dynamically fills an array from 5 to 50 with steps 5
print(np.arange(5, 50, 5))

# Creates a bidimentional array with an specific value
print(np.full((3, 5), 10))

# Lets create a diagonal inside a bidimentional array
print(np.diag([1, 3, 9, 10]))
