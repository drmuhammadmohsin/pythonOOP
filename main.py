from car import Car
from point import Point   
person1 = Car("Mohsin", "28", "Computer", "Pakistan")
person2 = Car("Cinzia", "45", "business", "italy")
person3 = Car("Amjad", "32", "economics", "para channar")

print(person1.age)
print(person2.name)
print(person3.work)

person1.sleep()
person2.eat()
person3.working()

print("This is mohsin check")