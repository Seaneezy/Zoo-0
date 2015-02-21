#general class for objects
class Things:
    pass
#is it living
class Dead(Things):
    pass
class Living(Things):
    pass
#is it an animal
class Animals(Living):
    pass
#is the animal a mammal or does it lay eggs(excluding platypi)
class Mammals(Animals):
    pass
#is the mammal large or small
class Large_Mammals(Mammals):
    pass
class Elephant(Large_Mammals):
    pass
class Gorilla(Large_Mammals):
    pass
class Zebra(Large_Mammals):
    pass
class Giraffe(Large_Mammals):
    pass
class Tiger(Large_Mammals):
    pass
class Small_Mammals(Mammals):
    pass
class Fox(Small_Mammals):
    pass
class Raccoon(Small_Mammals):
    pass
class Monkey(Small_Mammals):
    pass
#does the animal lay eggs
class Lays_Eggs(Animals):
    pass
#is the animal that lays eggs a Reptile
class Reptiles(Lays_Eggs):
    pass
class Snake(Reptiles):
    pass
#is the animal that lays eggs a Fish
class Fish(Lays_Eggs):
    pass
class Flounder(Fish):
    pass
class Long_Nose_Butterfly(Fish):
    pass
#is the animal that lays eggs a Bird
class Bird(Lays_Eggs):
    pass
class Parrot(Bird):
    pass
class Hummingbird(Bird):
    pass
class Flamingo(Bird):
    pass

