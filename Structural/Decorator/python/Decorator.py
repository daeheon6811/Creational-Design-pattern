class Animal:
  def speak(self):
    pass

class Cat(Animal):
  def speak(self):
    print("meow", end='')

class Dog(Animal):
  def speak(self):
    print("bark", end='')

def makeSpeak(animal:Animal):
  animal.speak()
  print(" ")
  

class Deco(Animal):
  def __init__(self,animal:Animal):
    self.animal = animal
  def speak(self):
    self.animal.speak()

class WthSmile(Deco):
  def speak(self):
    self.animal.speak()
    print("😀",end='')

class WthHeartEyes(Deco):
  def speak(self):
    self.animal.speak()
    print("😍",end='')


kitty = Cat()
makeSpeak(kitty)
kitty_smile = WthSmile(kitty)
makeSpeak(kitty_smile)
kitty_smile_heart = WthHeartEyes(kitty_smile)
makeSpeak(kitty_smile_heart)



dog = Dog()
makeSpeak(dog)
dog_heart = WthHeartEyes(dog)
makeSpeak(dog_heart)
dog_heart_smile = WthSmile(dog_heart)
makeSpeak(dog_heart_smile)