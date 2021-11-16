#일반적인 Cat class 정의
class Cat:
  def __init__(self):
    self.color = None
    self.eye_color = None
    self.nose_color = None
    self.tail_color = None
    self.name = None
    
#위 클래스를 이용한 같은 object를 만들고 싶을때
kitty = Cat()
kitty.color = 'white'
kitty.eye_color = 'white'
kitty.nose_color = 'white'
kitty.tail_color = 'white'
kitty.name = 'kitty'

nabi = Cat()
nabi.color = 'white'
nabi.eye_color = 'white'
nabi.nose_color = 'white'
nabi.tail_color = 'white'
nabi.name = 'nabi'