class Dog():
    def __init__(self, name, age, breed = 'unknown'):
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self):
        return f"a {self.age}-year-old {self.breed} called {self.name}"
    
    def __int__(self):
        return self.age
    
    def __bool__(self):
        return self.breed != ""
    
    def __add__(self, dog2):
        return Dog(self.name + dog2.name, self.age + dog2.age, self.breed)
    
    def __repr__(self):
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"

if __name__ == '__main__':
    fido = Dog('fido', 5, 'labrador') # Dog.__new__() gets called and returned Dog is passed to Dog.__init__(...)
    spot = Dog('spot', 3, "beagle")
    print(str(fido))
    print(int(fido) * 2)
    if fido:
        print("Fido is true")
    print(fido + spot)
    print(eval(fido.__repr__()))
