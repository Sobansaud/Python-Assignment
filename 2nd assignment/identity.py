x = [1, 2, 3]
y = [1, 2, 3]

# is - checks if both variables point to the same object
print(x is y)  # Output: False (x and y are different objects in memory)

# is not - checks if both variables do not point to the same object
print(x is not y)  # Output: True (x and y are different objects)

# Checking identity for same object
z = x
print(x is z)  # Output: True (x and z point to the same object)
