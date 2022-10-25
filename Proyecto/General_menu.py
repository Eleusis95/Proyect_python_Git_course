from Classes.persona import Person
from Classes.listado import listado
print("1.- Agrega una nueva persona")
print("2.- Eliminar a una persona")
print("3.- Buscar a una perosna")
option = input("Elige una de las opciones")

match option:
    case '1':
        print("Ingresa los datos de la persona")
        name = input("name : ")
        last_name = input("last name : ")
        age = input("age : ")
        address = input("address : ")
        new_person = Person(name,last_name,age,address)
        print(new_person.get_generla_infomation())
        my_list = listado(new_person)
        my_list.get_listado_items()

    