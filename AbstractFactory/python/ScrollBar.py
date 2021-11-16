#Scrollbar abstract(interface) and its implementations
class ScrollBar:
  def scroll(self):
    pass

class DarkScrollBar(ScrollBar):
  def scroll(self):
    print("dark scroll")

class LightScrollBar(ScrollBar):
  def scroll(self):
    print("light scroll")