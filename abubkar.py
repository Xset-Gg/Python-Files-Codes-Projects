class myclass:
    x =5
    print(x)

p1 = myclass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("ALI", 12)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("KHAN", 12)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("ABUBKAR", 30, "ali", "AZAN")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("ABUKAR", 12)
p1.greet()

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("abu", 12)
p1.greet()


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("king", 30)

del p1.age

print(p1.name)



class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "khan"

print(p1.name)
print(p1.age)
print(p1.city)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Ali", "ABUBKAR")
x.printname()