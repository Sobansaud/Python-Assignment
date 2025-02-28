ALL DATA TYPES WITH EXAMPLE IN PYTHON

"""
1. int
2. float
3. complex
4. list
5. tuple
6. range
7. str
8. set
9. frozenset
10. dict
11. bool
12. bytes
13. bytearray
14. memoryview
15. NoneType
"""




# 1. int
#Age of a person
age = 25
print("int (age):", age)



# 2. float
#Price of an item
price = 19.99
print("float (price):", price)




# 3. complex
#Complex number in mathematics (real + imaginary part)
complex_num = 4 + 5j
print("complex (complex number):", complex_num)




# 4. list
#List of student names
students = ['Alice', 'Bob', 'Charlie', 'David']
print("list (students):", students)




# 5. tuple
#Coordinates of a location (latitude, longitude)
location = (40.7128, -74.0060)  # New York City
print("tuple (location):", location)




# 6. range
#Generating numbers for a loop (1 to 5)
numbers = range(1, 6)
print("range (numbers):", list(numbers))  # Converting range to list for display




# 7. str
# A sentence
greeting = "Good Morning, everyone!"
print("str (greeting):", greeting)




# 8. set
# Unique items in a shopping cart (no duplicates allowed)
shopping_cart = {'apple', 'banana', 'orange', 'apple'}
print("set (shopping cart):", shopping_cart)




# 9. frozenset
#Set of allowed actions in a game (immutable)
allowed_actions = frozenset(['jump', 'run', 'attack'])
print("frozenset (allowed actions):", allowed_actions)




# 10. dict
#Storing employee information with keys as attributes
employee = {'name': 'John', 'age': 30, 'position': 'Software Engineer'}
print("dict (employee info):", employee)



# 11. bool
#Checking if a user is logged in
is_logged_in = True
print("bool (is logged in):", is_logged_in)



# 12. bytes
#Raw binary data (text encoded in bytes)
data = b'hello world'
print("bytes (data):", data)




# 13. bytearray
#Mutable sequence of bytes (modifying a byte array)
byte_data = bytearray([65, 66, 67])
byte_data[0] = 68  # Changing first byte to 'D'
print("bytearray (modified data):", byte_data)



# 14. memoryview
#Memory view of a byte object (efficiently accessing large binary data)
data_view = memoryview(b'hello')
print("memoryview (data view):", data_view)



# 15. NoneType
#A function returning nothing (no value)
def my_function():
    return None

result = my_function()
print("NoneType (function result):", result)
