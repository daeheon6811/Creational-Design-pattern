class DogBreedDNA:
  def __init__(self,breed,DNA):
    self.breed = breed
    self.DNA = DNA
  def __repr__(self):
    return f'{self.DNA}'

class Dog:
  DNA_Table = {}  #{key,DogBreedDNA} # 해쉬Set 구조
  @staticmethod
  def addDNA(breed,DNA):
    breed_DNA = DogBreedDNA(breed,DNA)
    Dog.DNA_Table[breed] = breed_DNA

  def __init__(self,name,age,gender,breed):
    self.name = name
    self.age = age
    self.gender = gender
    self.breed = breed
    if breed not in Dog.DNA_Table:
      raise RuntimeError(f"{breed} is not in DNA_Table")

  def __repr__(self):
    return f'{self.name},{self.age},{Dog.DNA_Table[self.breed]}'


Dog.addDNA('shihTzu','ATAGGCTTACCGATGG...')
Dog.addDNA('jinDo','ATAGGCTTACCGATGA...')

choco = Dog('choco',2,'male','shihTzu')
baduk = Dog('baduk',3,'female','jinDo')

print(choco)
print(baduk)

# bbobbi = Dog('bbobbi',1,'female','shiba') Error

# ---------------------------------------------------------------------------
# RuntimeError                              Traceback (most recent call last)
# <ipython-input-34-e301b9e75211> in <module>()
# ----> 1 bbobbi = Dog('bbobbi',1,'female','shiba')

# <ipython-input-32-e63efbb45611> in __init__(self, name, age, gender, breed)
#      20     self.breed = breed
#      21     if breed not in Dog.DNA_Table:
# ---> 22       raise RuntimeError(f"{breed} is not in DNA_Table")
#      23 
#      24   def __repr__(self):

# RuntimeError: shiba is not in DNA_Table