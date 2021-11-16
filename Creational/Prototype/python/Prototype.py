#deepcopy(clone) 지원 cat
import copy

class Cat:
  def __init__(self):
    self.color = None
    self.eye_color = None
    self.nose_color = None
    self.tail_color = None
    self.name = None

  def clone(self):
    return copy.deepcopy(self)
  
cat_basic = Cat()
cat_basic.color = 'white'
cat_basic.eye_color = 'white'
cat_basic.nose_color = 'white'
cat_basic.tail_color = 'white'
cat_basic.name = 'kitty'

kitty = cat_basic.clone()
kitty.name = 'kitty'

nabi = cat_basic.clone()
nabi = 'nabi'

#잘못된 복사방법
#nabi = kitty

#abstract structure prototype
class BlackCat(Cat):
  def __init__(self):
    super().__init__()
    self.color = 'black'

class WhiteCat(Cat):
  def __init__(self):
    super().__init__()
    self.color = 'white'


black_cat = BlackCat()
black_cat.nose_color = 'pink'
black_cat.tail_color = 'green'

#black_cat is prototype
kitty = black_cat.clone()
kitty.eye_color = 'white'
kitty.name = 'kitty'

nabi = black_cat.clone()
nabi.eye_color = 'blue'
nabi.name = 'nabi'