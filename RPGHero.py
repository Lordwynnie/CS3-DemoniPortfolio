class Hero:
  def __init__(self, name, hp): #attributes
    self.name = name
    self.__hp = hp

  def take_damage(self, amount): #methods
    self.__hp -= amount

  def get_hp(self):
    return self.__hp


  def __repr__(self):
    return f"I'm {self.name} with {self.__hp} HP!"


h = Hero("Arthur", 100)
h.take_damage(10)
print(h)
h = Hero("Morgana", 100)
print(h)