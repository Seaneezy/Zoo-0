import random

class Mammal:
    pass
class Ape(Mammal):
    def hang(self):
        print(self) + " is lounging under a tree"
class Monkey(Ape):
    def __init__(self,name):
        print("Just created a monkey")
class Gorilla(Ape):
    def __init__(self):
        print("Just created a Gorilla")
class Tiger(Mammal):
    def __init__(self, name, age, weight, stripes):
        self.name=name
        self.age=age
        self.weight=weight
        self.stripes=stripes
        print("Just created a tiger called " + name + ".")
        print(name + " weighs "+ str(weight)+ "lbs and has "+str(stripes) + " stripes.")
    def lounge(self):
        print(self.name + " is lounging under a tree")
sher = Tiger("Sher Khan", 20, 300,50)
sha = Tiger("Sha Khan", 14, 260,38)
dar = Tiger("Dar Khan", 19, 280,40)
Caesar=Gorilla()
dar.lounge()
