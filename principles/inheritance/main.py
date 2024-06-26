# Super or Base Class
class DuckSuperClass:
    def quack(self):
        print("Quack Quack!")
        
    def swim(self):
        print("Swimming Hard!")
        
    def fly(self):
        print("Flying Hard!")
    
    def display(self):
        print("Im a Duck!")
        
class MallardDuck(DuckSuperClass):
    # Overrides Duck Display Trait
    def display(self):
        print("Im a Mallard Duck!")
        
class RedHeadDuck(DuckSuperClass):
    def display(self):
        print("Im a Red-Head Duck!")
        
class RubberDuck(DuckSuperClass):
    def display(self):
        print("Im a Rubber Duck!")

    # Overrides Duck Quack Trait
    def quack(self):
        print("Squeak Squeak!")
    
    # Overrides Duck Fly Trait
    def fly(self):
        print("Sadly I Cannot Fly!")
        
md = MallardDuck()
rhd = RedHeadDuck()
rd = RubberDuck()

for duck in (md, rhd, rd):
    duck.display()
    duck.quack()
    duck.swim()
    duck.fly()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")