class Dog:
    
    def __init__(self, name, breed):
        self.Name = name
        self.Breed = breed
    
    
    def bark(self):
        print("Woof woof")
        
dog1 = Dog("Bruce", "Scottish Terrier")
dog1.bark()
print(dog1.Name)
print(dog1.Breed)

dog2 = Dog("Freya", "Greyhound")
dog2.bark()
print(dog2.Name)
print(dog2.Breed)