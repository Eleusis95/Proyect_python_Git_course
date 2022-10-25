import cofig
from Classes.persona import Person
print("1.- Agrega una nueva persona")
print("2.- Eliminar a una persona")
print("3.- Buscar a una perosna")
option = input("Elige una de las opciones")
listado_person = {}
match option:
    case '1':
        print("Ingresa los datos de la persona")
        name = input("name : ")
        last_name = input("last name : ")
        age = input("age : ")
        address = input("address : ")
        new_person = Person(name,last_name,age,address)
        print(new_person.get_generla_infomation())
        cofig.items_counter+=1
        listado_person[str(cofig.items_counter)] = new_person


        print(listado_person[str(cofig.items_counter)])
       

    