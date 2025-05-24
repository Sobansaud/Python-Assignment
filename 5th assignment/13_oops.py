# CLASSES AND INSTANCE VARIABLES

class Student:
    school_name = "Beaconhouse"   # Class variable

    def __init__(self,name):
        self.name = name   # Instance variable
    

s1 = Student("John")
s2 = Student("Alice")
s3 = Student("Bob")
s4 = Student("Charlie")
s5 = Student("David")
print(s1.name,s2.name,s3.name,s4.name,s5.name)

print(s1.school_name)
s1.name = "Ahmed"
print(s1.name,s2.name,s3.name,s4.name,s5.name)
 
Student.school_name = "falconhouse"
print(s1.school_name)


# COMPOSITION AND AGGREGATION

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

c1 = Car()
c1.start_car()

# AGGREGATION

class Student:
    def __init__(self,name):
        self.name = name
    

class School:
    def __init__(self,students):
        self.students = students

s1 = Student("Ahemd khan")
s2 = Student("Saleem khan")
my_school = School([s1,s2])
del my_school

print(s1.name)


#  MEHTOD RESOLUTION ORDER

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")
    
class D(B,C):
    pass

d = D()
print(d.greet())
print(D.mro())


# DECORATORS IN CLASS

# function decorator


def myclass(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@myclass
def hello():
    print("★★★★★  Assalamuwalikum how are you class!  ★★★★★")

hello()


# class decorator

class Objectcounter:
    def __init__(self, cls):
        self.cls = cls
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"Instance number {self.count}")
        return self.cls
    
@Objectcounter
class MyClass:
    pass

a = MyClass()
b = MyClass()
c = MyClass()


#  PROPERTY DECORATOR

#  GETTER

class Card_Access:
    def __init__(self, name, card_number, __pin):
        self.name = name
        self.card_number = card_number
        self.__pin = __pin

    @property
    def pin(self):
        return self.__pin

p = Card_Access("John", "123456789", 1234)
print(p.pin)

#  SETTER

class Person:
    def __init__(self,__name):
        self.__name = __name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name= value

n = Person("John")
n.name = "Jane"
print(n.name)

#  DELETER

class Car:
    def __init__(self,name,__price):
        self.name = name
        self.__price = __price

    @property
    def price(self):
        return self.__price
    
    @price.deleter
    def price(self):
        del self.__price

pr = Car("Toyota", 50000)
print(pr.price)
# del pr.__price

#  COMPUTED PROPERTIES

class Person:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)
    
p = Person(5.5,70)
print(p.bmi)


# CALLABLE OBJECT

class Person:
    def __call__(self,name):
        print(f"Hello How Are You {name}")
    
p = Person()
p("Soban")



        


