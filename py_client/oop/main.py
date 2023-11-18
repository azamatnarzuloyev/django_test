# import logging
# logging.warning("salom")
# class Car:
#     yosh  = 100

# class Person:
#     def __init__(self , name, age):
#         self.name = name
#         self.age = age

#     def intrducs(self):
#         return f"{self.name} {self.age}"
    
#     @staticmethod
#     def createarticel():
#         return Car
    

# person = Person.createarticel()

# class TestClass:
#     product = 22
#     def __init__(self , name, age):
#         self._yosh = 210
#         self.name = name, 
#         self.__age = age

    
#     def hello(self):
#         return (self.__age - TestClass.product) if (TestClass.product) > 100  else self._yosh
    

    
#     def __str__(self):
#         return f"{self.name} str"
    
#     def __repr__(self):
#         return f"{self.name} repr"
    

# test = TestClass('azamat',21)
# print(test)
# arr = ["salom", "hello", "book"]

# data = hasattr(arr, 'salom')
# print(data)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)
    
person = Person("azamat",34)

print(person.age)