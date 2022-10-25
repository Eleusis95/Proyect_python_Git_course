from persona import Person

class Alumno(Person):

    def __init__(self,name,last_name, age,address,school,year):
        self.school = school
        self.year = year
        Person.__init__(self,name, last_name, age, address)
    def __get_school(self):
        return self.school
    def __get_year(self):
        return self.year

    def __str__(self):
        return f"{Person.__str__(self)} and studies at school : {self.__get_school()} and is in {self.__get_year()}"

myalumno = Alumno(name = "Juan",last_name = "Lopez",age =12,address ="Jesus Garcia #45",school="Enrique Diaz de Leon",year=5)
print(myalumno)