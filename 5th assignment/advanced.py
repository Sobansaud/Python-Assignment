# advanced oops

# META CLASS

class Meta(type):
    def __new__(cls,name,bases,dct):
        print(f"Creating new class {name}")
        return super().__new__(cls,name,bases,dct)
    
class Person(metaclass=Meta):
    pass

#  Singleton Pattern – Sirf 1 Instance banega

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
a = Singleton()
b = Singleton()
print(a is b)

# Factory Pattern – Cheezon ko flexible banaye

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Factory:
    @staticmethod
    def create(animal_type):
        if animal_type == "dog":
            return Dog()
        if animal_type == "cat":
            return Cat()
        raise ValueError(" Invalid animal type")
    
a = Factory.create("dog")
print(a.speak())



#  Error Handling in OOP

class Insufficient(Exception):
    def __init__(self,balance,amount):
        super().__init__(f" Insufficient balance. Current balance is {balance} and you are trying to withdraw {amount}")

class Bank:
    def __init__(self,acc_holder,balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount
    
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if self.balance < amount:
            raise Insufficient(self.balance,amount)
        self.balance -= amount


acc = Bank("Ali",10000)
try:
    acc.withdraw(5000)
    print (acc.balance)
except Insufficient as e:
    print(e)

#  Testing OOP Code

# SIMPLE CALCULATOR

class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a/b
c = Calculator()
print(c.add(5,3)) 
print(c.subtract(5,3))  
print(c.multiply(5,3))  
print(c.divide(5,15))

# UNITTEST
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


import pytest

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)


