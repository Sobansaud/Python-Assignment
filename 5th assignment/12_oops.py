# ENCAPSULATION

class Car:
    def __init__(self,bankname,_balance,__pin):
        self.bankname = bankname
        self._balance = _balance
        self.__pin = __pin

    def get_deposit(self):
        return self.__pin
    
    def set_deposit(self):
        self.__pin = 1234

c = Car("soban", 1000, 1234)
print(c.get_deposit())

# ABSTRACTION
class Car:
    def __init__(self,engine,color):
        self.engine = engine
        self.color = color
    
    def start(self):
        print("Car has been Started")

c2 = Car("V8", "Red")
c2.start()


# INHERITANCE

class Parent:
    def __init__(self,hobby):
        self.hobby = hobby
    
class Child(Parent):
    def __init__(self,hobby,age):
        super().__init__(hobby)
        self.age = age


class Senior:
    def __init__(self,cricket):
        self.cricket = cricket
    
class Junior(Senior):
    def __init__(self,cricket):
        super().__init__(cricket)

cri = Junior("Batting")
print(cri.cricket)


c = Child("Cricket",20)
print(c.hobby)

#  POLYMORPHISM

class Dog:
    def speak(self):
        print("Barking ")
    
class Cat:
    def speak(self):
        print("Meowing ")

class Hen:
    def speak(self):
        print("KUKRUKU ")

def sound(animal):
    animal.speak()

sound(Cat())
sound(Dog())
sound(Hen())


# CLASS AND OBJECTS

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def hello(self):
        print(f"My Name Is {self.name} And My Age Is {self.age} And My Salary is {self.salary}")

    def __del__(self):
        print("Employee Details has been deleted")

person = Employee("Abhinandan",20,10000)
person.hello()

del person


# METHOD OVERRIDING

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return "Aniaml Sound"
    
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def sound(self):
        return "Bow Bow"
    
override = Dog("German Shepard")
print(override.sound())


# OPERATOR OVERLOADING


class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Points(self.x + other.x , self.y + other.y)
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Points(1,2)
p2 = Points(3,5)
p3 = p1 + p2
print(p3)


# DUCK TYPING

class Duck:
    def speak(self):
        return self.__repr__()+ ": Quack !"
    
class Person:
    def speak(self):
        return self.__repr__() + " : I can also quack like a duck!"

def makeit_quack(duck):
    print(duck.speak())

duck = Duck()
person = Person()

makeit_quack(duck)
makeit_quack(person)



class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}")

c1 = Car("Sonata",2025)
c1.start_engine()



class Bank:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        
    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = Bank(1000)
acc.deposit(100)
acc.withdraw(0)
print(acc.get_balance())


class Parent:
    def __init__(self,amount):
        self.amount = amount

class Child1(Parent):
    def __init__(self,amount):
        super().__init__(amount)
    
class Child2(Parent):
    def __init__(self,amount):
        super().__init__(amount)

class Child3(Parent):
    def __init__(self,amount):
        super().__init__(amount)


parents = Parent(7500)
c1 = Child1(2500)
c2 = Child2(2500)
c3 = Child3(2500)
print(c1.amount,c2.amount,c3.amount)


class Animal():
    def move(self):
        print("Moving...")

class Dog(Animal):
    def move(self):
        print("Barking...!")

class Cat(Animal):
    def move(self):
        print("Meowing...!")

def make_sound(animal):
    animal.move()

make_sound(Dog())
make_sound(Cat())

class Car:
    def drive(self):
        print("Driving...")

class Bike(Car):
    def drive(self):
        print("Riding...")

class Truck(Car):
    def drive(self):
        print("Driving...")

def drive_vehicle(vehicle):
    vehicle.drive()

drive_vehicle(Truck())
drive_vehicle(Bike())



from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

car = Car()
bike = Bike()
car.start_engine()
bike.start_engine()



# INSTANCE METHODS

class Boy:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello , my name is {self.name}")

b1 = Boy("Soban")
b1.greet()

#  CLASS METHODS

class Student:
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        print(f"Total Students in this class is : {cls.count}")

number = Student("Soban")
numbers = Student("Noaman")
numbers = Student("Affan")
numbers.get_count()


# STATIC METHODS

class Math:
    @staticmethod
    def add(a,b):
        return a * b

print(Math.add(5,5))


# PRACTICE QUESTION

class Books:
    count = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Books.count += 1

    def book_info(self):
        print(f"The title of the book is {self.title} and the author is {self.author}")

    
    @classmethod
    def get_count(cls):
        print(f"Totals books : {cls.count}")

    @staticmethod
    def count_characters(title):
        return len(title)
    
book = Books("Python Programming","Soban")
book.book_info()
book = Books("Java Script ","Soban")
book.book_info()
book.get_count()
print(Books.count_characters("Python Programming"))
print(Books.count_characters("Java Script"))


# 2ND PRACTICE Q/A
class Book:
    count = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.count += 1

    def info(self):
        print(f"The title of the book is {self.title} and the author is {self.author}")

    @classmethod
    def display_total(cls):
        print(f"Total books : {cls.count}")
    
    @staticmethod
    def is_title_long(title):
        if len(title) > 10:
            return True
        
class Ebook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size

    def info(self):
        super().info()
        print(f"The file size of the ebook is {self.file_size} MB")

class Printedbook(Book):
    def __init__(self,title,author,pages):
        super().__init__(title,author)
        self.pages = pages

    def info(self):
        super().info()
        print(f"The number of pages in the printed book is {self.pages}")

b1 = Book("Typescript Programming","Soban")
b1 = Book("Python Programming","Soban")
b1 = Book("C++ Programming","Soban")
ebook = Ebook("Pyhton Crash Course", "Soban", 10)
pbook = Printedbook("Python Programming", "Soban", 200)

b1.info()
ebook.info()
pbook.info()

b1.display_total()
print(Book.is_title_long("Typescript Programming"))





    