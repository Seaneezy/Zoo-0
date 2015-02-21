class Mammal:
    def feed_milk_to_young(self):
        pass
    def drink(self,substance):
        print(self.name + " is drinking "+substance)
class Ape(Mammal):
    def eat_banana(self):
        print(self.name + " is eating a banana")
class Monkey(Ape):
    def __init__(self,name,age,weight,tail):
        self.name=name
        self.age=age
        self.weight=weight
        self.tail=tail
        print("Just created a monkey called "+name+ ".")
        print(name + "'s tail is "+str(tail)+ "ft long.")
    def hang_by_tail(self):
        print(self.name + " is hanging by it's tail")
class Gorilla(Ape):
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
        print("Just created a gorilla called "+name+".")
class Tiger(Mammal):
    def __init__(self,name,age,weight,stripes):
        self.name=name
        self.age=age
        self.weight=weight
        self.stripes=stripes
        print("Just created a tiger called "+name + ".")
        print(name+" weighs "+str(weight)+ "lbs and has "+str(stripes)+" stripes.")
    def lounge(self):
        print(self.name + " is lounging under a tree")
    def play(self,tiger2):
        self.tiger2=tiger2
        print(self.name + " is playing with "+str(tiger2) )

sher=Tiger("Sher Khan",20,300,50)
balu=Monkey("Balu",10,50,2)
tony=Tiger("Tony the Tiger",22,310,46)
balu.eat_banana()
balu.hang_by_tail()
"""
print(sher.age)
print(sher.name)
print(sher.weight)
"""
sher.drink("water")
sher.play(tony.name)

justin=Tiger("Bustin Jieber",10,200,35)
justin.lounge()