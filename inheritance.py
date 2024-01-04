
class pet:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age}")
    
    def speak(self):
        print("I dont know what to say!!!")

class dog(pet):
    def speak(self):
        print("Meow")
    
class cat(pet):
    def speak(self):
        print("bark")

p=pet("Tim",19)
p.speak()
c=cat("jill",19)
c.speak()
d=dog("don",13)
d.speak()