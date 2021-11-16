class Animal:
  def speak(self):
    pass

class Cat(Animal):
  def speak(self):
    print('a cat ',end='')

class Dog(Animal):
  def speak(self):
    print('a dog ',end='')
    

class Vehicle:
  def __init__(self,animal:Animal):
    self.animal = animal

  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    self.animal.speak()
    print('drives a car')

class Boat(Vehicle):
  def start(self):
    self.animal.speak()
    print('sails a boat')

class Airplane(Vehicle):
  def start(self):
    self.animal.speak()
    print('flies a plane')
    
cat = Cat()
boat = Boat(cat)
boat.start()


dog = Dog()
car = Car(dog)
car.start()