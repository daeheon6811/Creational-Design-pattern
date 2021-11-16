class Dog:
  DNAseq = "ATAGGCTTACCGATGG...."
  def __init__(self,name,age,gender,breed):
    self.name = name       #<20bytes ,upto 20 chars
    self.age = age         #8bytes   ,64bit integer
    self.gender = gender   #1byte    
    self.breed = breed     #2bytes   ,upto 65k breeds

  def __repr__(self):
    return f'{self.name},{self.age},{Dog.DNAseq}'


choco = Dog('choco',2,'male','shihTzu')
baduk = Dog('baduk',3,'female','jinDo')

print(choco)
print(baduk)