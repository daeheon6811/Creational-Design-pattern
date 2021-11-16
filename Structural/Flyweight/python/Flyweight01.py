class Dog:
  def __init__(self,name,age,gender,breed,DNA):
    self.name = name       #<20bytes ,upto 20 chars
    self.age = age         #8bytes   ,64bit integer
    self.gender = gender   #1byte    
    self.breed = breed     #2bytes   ,upto 65k breeds
    self.DNA = DNA   #MBytes

  def __repr__(self):
    return f'{self.name},{self.age},{self.DNA}'

choco = Dog('choco',2,'male','shihTzu','ATAGGCTTACCGATGG...')
baduk = Dog('baduk',3,'female','jinDo','ATAGGCTTACCGATGG...')

print(choco)
print(baduk)