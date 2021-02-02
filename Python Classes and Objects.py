class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking...')

    def speak(self):
        print('Hello my name is ' + self.name + ' and i am ' + str(self.age) + ' years old ' )

peter = Person('Peter', 51)
gordon = Person('Gordon', 49)

print(peter.name + ' ' +str(peter.age))
peter.speak()
peter.walk()

print(gordon.name + ' ' +str(gordon.age))
gordon.speak()
gordon.walk()