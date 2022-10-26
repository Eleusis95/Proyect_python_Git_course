from persona import Person

class Profesor(Person):
    def __init__(self,name,last_name, age,address,matter,school):
        self.matter = matter
        self.school = school
        Person.__init__(self,name,last_name, age,address)
    def __str__(self):
        return f"{Person.__str__(self)} and teachs the matter : {self.matter} at school {self.school}"

myprofesor = Profesor(name="Pedro",last_name="Lopez",age=85,address="Alcalde #43",matter="History",school="Enrique díaz")

print(myprofesor)