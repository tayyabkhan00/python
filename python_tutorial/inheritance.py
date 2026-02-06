class animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        return f"the sound of {self.name}"

    def eat(self):
        print(f"{self.name} is eating")
    
    def run(self):
        print(f"the {self.name} is running")
class cat(animal):
    def sound(self):
        return super().sound() + " is meow"

c=cat("billa")
print(c.sound())
c.eat()
c.run()

