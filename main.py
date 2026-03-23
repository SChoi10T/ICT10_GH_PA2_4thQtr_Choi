# Dog Form
from pyscript import display, document # pyright: ignore[reportMissingImports]


class Dog:
    def __init__(self, breed, age, name, owner):
        self.breed = breed
        self.age = age
        self.name = name
        self.owner = owner

    
    def bark(self): # creating a method
        display('Arf '*3, target='output')

# Form
class ChildDog(Dog):
        pass

def displaying_info(e):
    name = document.getElementById('name').value
    breed = document.getElementById('breed').value
    owner = document.getElementById('owner').value
    age = document.getElementById('age').value

    document.getElementById('output').innerHTML = ''

    dogform = ChildDog(name, breed, owner, age)

    display(f'{dogform.name}, {dogform.breed}, {dogform.owner}, {dogform.age}', target='output')