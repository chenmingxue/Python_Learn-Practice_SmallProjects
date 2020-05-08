# Source: https://www.geeksforgeeks.org/abstract-classes-in-python/
#By default, Python does not provide abstract classes. 
#Python comes with a module which provides the base for defining Abstract Base classes(ABC) 
#and that module name is ABC. ABC works by decorating methods of the base class as abstract 
#and then registering concrete classes as implementations of the abstract base. 
#A method becomes abstract when decorated with the keyword @abstractmethod.

# example 1
from abc import ABC, abstractmethod 
  
class Animal(ABC): 
    def move(self): 
        pass

class Human(Animal): 
    def move(self): 
        print("I can walk and run") 

class Snake(Animal): 
    def move(self): 
        print("I can crawl") 

        
class Dog(Animal): 
    def move(self): 
        print("I can bark") 

        
class Lion(Animal): 
    def move(self): 
        print("I can roar") 

R = Human() 
R.move() 
  
K = Snake() 
K.move() 
  
R = Dog() 
R.move() 
  
K = Lion() 
K.move()

# example 2
# no need to explicitly call abc
class parent:        
    def geeks(self): 
        pass

class child(parent): 
    def geeks(self): 
        print("child class") 

R = child()
R.geeks()

# example 3
# use super() to call properties or function

import abc 
from abc import ABC, abstractmethod 
  
class R(ABC): 
    def rk(self): 
        print("Abstract Base Class") 
  
class K(R): 
    def rk(self): 
        super().rk() 
        print("subclass ") 

r = K() 
r.rk() 










