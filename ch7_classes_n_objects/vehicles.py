class Foo():
    def __init__(self,x,y):
        print(x + y)
        
f = Foo(3,4)

print("funfou 1")

class Vehicle:
    name = "Jeep"
    kind = "car"
    color = "Blue"
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
        
#your code goes here
#car1 = Vehicle("Summer Jeep", "renegade", "crimson red", 100.00)
#car1.name = "Summer Jeep"
#car1.kind = "renegade"
#car1.color = "crimson red"
#car1.value = 100.00
car1 = Vehicle()
#test code
print(car1.value)
print(car1.description())
#print(car2.description)
    