# LIST , TUPLES AND DICTIONARY

# LISTS

fruits : list = ["apple" , "banana" , "mango" , "orange" , "kiwi" , "grapes"]
print(fruits)
print(fruits[-3])    # prints the 3rd last element
print(fruits[2:5])    # from index 2 to 5
print(len(fruits))   # length of the list

fruits[-3] = "strawberry"    # replace the 3rd last element with strawberry
print(fruits)

fruits.append("cherry")    # add an element at the end of the list
print(fruits)

fruits.extend(["papaya" , "lemon"])   # add multiple elements at the end of the list
print(fruits)

fruits.count("apple")    # count the number of times "apple" appears in the list
print(fruits)

fruits.remove("banana")    # remove the first occurrence of "banana" in the list
print(fruits)

fruits.pop(3)    # remove the element at index 3 and return it
print(fruits)    # remove cherry


numbers = [1,6,3,9,2,5,4,8,7,10]
numbers.sort()
print(numbers)  # prints the list in ascending order

numbers.sort(reverse=True)
print(numbers)  # prints the list in descending order

numbers.reverse()
print(numbers)  # prints the list in reverse order

for apple in fruits:
    print(apple)
else:
    print("fruits was found")






# TUPLES

tuple1 = (1,2,34,5,6,75)
print(tuple1[1])
print(tuple1[0:5])
print(len(tuple1))



tuple2 = (1,2,34,5,6,75) + (7,8,9,10,11,12)
print(tuple2)

tuple3 = tuple1 * 2
print(tuple3)




# DICTIONARY

my_dict: dict = {
    "name": "Soban",
    "age": 17,
    "city": "Karachi",
    "country": "Pakistan",
    "hobbies": ["reading", "swimming", "coding"],
    "address": "123, Street 1, Karachi, Pakistan",
    "gender": "male",
    "isStudent": True
}
print(my_dict)
my_dict["name"] = "Noaman"
print(my_dict)
print(my_dict["name"])

del my_dict["address"]
print(my_dict)
