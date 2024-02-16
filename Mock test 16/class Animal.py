class Animal:

    @classmethod
    def eat(cls):
        print("Animals can eat.")
class Herbivore(Animal):
    # def __init__(self,stomach):
    #     self.stomach = stomach
    def eat(self,leafs):
        print("herbivorous animals eat:",leafs)
class Carnivore(Animal):
    # def __init__(self):

    def eat(self,meat):
        print("carnivorous animals eat:",meat)

tiger = Carnivore()
tiger.eat('meat')
goat = Herbivore()
goat.eat('leaf')
Animal.eat()