from project.dog import Dog
from project.cat import Cat
from project.kitten import Kitten
from project.tomcat import Tomcat

dog = Dog("Buddy", 3, "Male")
cat = Cat("Misty", 2, "Female")
kitten = Kitten("Luna", 1)
tomcat = Tomcat("Tom", 5)

print(dog)
print(dog.make_sound())

print(cat)
print(cat.make_sound())

print(kitten)
print(kitten.make_sound())

print(tomcat)
print(tomcat.make_sound())
