class Cat:
  def speak(self):
    print("meow")


kitty = Cat()
kitty.speak()

class CatProxy:
  def __init__(self, cat:Cat):
    self.cat = cat

  def speak(self):
    print("\nbefore speak") #validity checks,lazy init, more
    self.cat.speak()
    print("after speak") #loggings

kitty_proxy = CatProxy(kitty)
kitty_proxy.speak()

class Animal: #interface class
  def speak(self):  
    pass

class Cat(Animal):
  def speak(self):
    print("meow")

class CatProxy(Animal):
  def __init__(self, cat:Cat):
    self.cat = cat

  def speak(self):
    print("before speak")
    self.cat.speak()
    print("after speak")

def doSpeak(animal:Animal):
  animal.speak()

kitty = Cat()
kitty_proxy = CatProxy(kitty)
doSpeak(kitty_proxy)