# SETS AND FROZENSETS

my_set1 = {1,2,3,4,5,6,7,8,9,10,1,2}
print(my_set1)
print(type(my_set1))

set2 = {1,2,3,"hello" , False , 9, "pakistan"}
print(set2)
set2.remove("hello")
print(set2)
set2.pop()   # removes the last element
print(set2)

my_set1.difference(set2)
print(my_set1)
my_set1.intersection(set2)
print(my_set1)
my_set1.union(set2)
print(my_set1)
my_set1.symmetric_difference(set2)
print(my_set1)






# frozenset1 = frozenset([1,2,21,4,6,8,54,"Hello" , "World"])
# print(frozenset1)
