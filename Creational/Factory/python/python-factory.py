from enum import Enum
class AnimalEnum(Enum):
  CAT = 1
  DOG = 2

class Animal():
  def speak(self):
    pass

class Cat(Animal):
  def speak(self):
    print("meow")

class Dog(Animal):
  def speak(self):
    print("bark")
    
#Factory function
#prefer enum


def FactoryFn(animal:AnimalEnum):
  if animal == AnimalEnum.CAT:
    return Cat()
  elif animal == AnimalEnum.DOG:
    return Dog()


cat = FactoryFn(AnimalEnum.CAT)
cat.speak()
dog = FactoryFn(AnimalEnum.DOG)
dog.speak()

#Factory class
class AnimalFactory():
  def createAnimal(self,animal):
    if animal == AnimalEnum.CAT:
      return Cat()
    elif animal == AnimalEnum.DOG:
      return Dog()

animal_factory = AnimalFactory()
cat = animal_factory.createAnimal(AnimalEnum.CAT)
cat.speak()
dog = animal_factory.createAnimal(AnimalEnum.DOG)
dog.speak()