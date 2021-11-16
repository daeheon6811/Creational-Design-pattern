#Button abstract(interface) and its implementations
class Button:
  def click(self):
    pass

class DarkButton(Button):
  def click(self):
    print("dark click")

class LightButton(Button):
  def click(self):
    print("light click")