from Button import *
from CheckBox import *
from ScrollBar import *


#UIFactory Abstract(interface) and its implementations
class UIFactory:
  def getButton(self):
    pass
  
  def getCheckBox(self):
    pass

  def getScrollBar(self):
    pass

class DarkUIFactory(UIFactory):
  def getButton(self):
    return DarkButton()

  def getCheckBox(self):
    return DarkCheckBox()

  def getScrollBar(self):
    return DarkScrollBar()

class LightUIFactory(UIFactory):
  def getButton(self):
    return LightButton()

  def getCheckBox(self):
    return LightCheckBox()

  def getScrollBar(self):
    return LightScrollBar()

#get darkTheme UI components
dark_factory = DarkUIFactory()
dark_btn = dark_factory.getButton()
dark_checkBx = dark_factory.getCheckBox()
dark_scrollBar = dark_factory.getScrollBar()

dark_btn.click()
dark_checkBx.check()
dark_scrollBar.scroll()

#get lightTheme UI components
light_factory = LightUIFactory()
light_btn = light_factory.getButton()
light_checkBx = light_factory.getCheckBox()
light_scrollBar = light_factory.getScrollBar()

light_btn.click()
light_checkBx.check()
light_scrollBar.scroll()