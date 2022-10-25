from persona import Person

class Profesor(Person):
    def __init__(self,name,last_name, age,address,matter):
        self.matter = matter
        Person.__init__(name,last_name, age,address)