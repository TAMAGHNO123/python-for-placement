class Dog:
    
    def __init__(self, name, breed):   #_init_ is a constructor having 2 attributes name and breed
        self.Name = name
        self.Breed = breed
    
    
    def bark(self):
        print("Woof woof")
        
dog1 = Dog("Bruce", "Scottish Terrier")   #--->The __init__ method is automatically called when creating dog1
dog1.bark()
print(dog1.Name)
print(dog1.Breed)

dog2 = Dog("Freya", "Greyhound")
dog2.bark()
print(dog2.Name)
print(dog2.Breed)



'''
---> self is a reference to the instance of the class.
---> It allows access to instance variables and instance methods.
---> Every time an object is created, self represents that specific object.



---> A class is like a blueprint, and an instance is a specific object built from that blueprint.
---> Each instance has its own set of data (attributes) and can use the methods defined in the class.
'''