class Person:
    def __init__(self, name, age):
         self.name = name
         self.age = age 

    def walk(self): 
        print(self.name + ' is walking...')

    def speak(self):
        print ('helo my name is ' + self.name + ' and i am ' + str(self.age) + ' years old')

john = Person('John', 22)
mariam = Person('Mariam', 18)

print (john.name + ' ' + str(john.age))
john.speak()
john.walk()
print (mariam.name + ' ' + str(mariam.age))
mariam.speak()
mariam.walk()