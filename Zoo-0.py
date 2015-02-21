
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
    def __init__(self):
        print("Made an elephant")
class Gorilla(Large_Mammals):
    def __init__(self):
        print("Made a Gorilla")
class Zebra(Large_Mammals):
    def __init__(self):
        print("Made a Zebra")
class Giraffe(Large_Mammals):
    def __init__(self):
        print("Made a Giraffe")
class Tiger(Large_Mammals):
    def __init__(self):
        print("Made a Tiger")
class Small_Mammals(Mammals):
    pass
class Fox(Small_Mammals):
    def __init__(self):
        print("Made a Fox")
class Raccoon(Small_Mammals):
    def __init__(self):
        print("Made a Raccoon")
class Monkey(Small_Mammals):
    def __init__(self):
        print("Made a Monkey")
#does the animal lay eggs
class Lays_Eggs(Animals):
    pass
#is the animal that lays eggs a Reptile
class Reptiles(Lays_Eggs):
    pass
class Snake(Reptiles):
    def __init__(self):
        print("Made a Snake")
#is the animal that lays eggs a Fish
class Fish(Lays_Eggs):
    pass
class Flounder(Fish):
    def __init__(self):
        print("Made a Flounder")
class Long_Nose_Butterfly(Fish):
    def __init__(self):
        print("Made a Long-Nose Butterfly")
#is the animal that lays eggs a Bird
class Bird(Lays_Eggs):
    pass
class Parrot(Bird):
    def __init__(self):
        print("Made a Parrot")
class Hummingbird(Bird):
    def __init__(self):
        print("Made a Hummingbird")
class Flamingo(Bird):
    def __init__(self):
        print("Made a Flamingo")

Nemo=Flounder()
PinkBird=Flamingo()
Tony=Tiger()
Swiper=Fox()
Caesar=Gorilla()
FishGuy=Long_Nose_Butterfly()
Fruit_Loops=Parrot()
Mammoth=Elephant()



