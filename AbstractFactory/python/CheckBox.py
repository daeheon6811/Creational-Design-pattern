#Checkbox abstract(interface) and its implementations
class CheckBox:
  def check(self):
    pass

class DarkCheckBox(CheckBox):
  def check(self):
    print("dark check")

class LightCheckBox(CheckBox):
  def check(self):
    print("light check")