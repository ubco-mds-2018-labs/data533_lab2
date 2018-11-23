class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name: {}, Age: {}, Gender: {}". format(self.name, self.age, self.gender))

class healthdata(Person):
    def __init__(self, name, age, gender, file):
        Person.__init__(self, name, age, gender)
        self.file = file

    def data(self):
        import pandas as pd
        self.data = pd.read_csv(self.file)
        Person.display(self)
        return self.data
