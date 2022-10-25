"""Module for Class Person"""


class Person():
    """"Class person, is the base for future classes"""

    def __init__(self,name,last_name, age,address):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address

    def get_generla_infomation(self):
        return f"name : {self.__get_name()}"\
        f"last name : {self.__get_last_name()}"\
        f"age : {self.__get_age()}"\
        f"address : {self.__get_address()}"
    def __get_name(self):
        return self.name
    def __get_last_name(self):
        return self.last_name
    def __get_age(self):
        return self.age
    def __get_address(self):
        return self.address

    def __set_name(self,new_name):
        self.name = new_name
    def __set_last_name(self,new_last_name):
        self.last_name = new_last_name
    def __set_age(self, new_age):
        self.age = new_age
    def __set_address(self,new_address):
        self.address = new_address

    def __str__(self):
        return f"{self.__get_name()}"\
        f"{self.__get_last_name()} is"\
        f"{self.__get_age()} and lives at"\
        f"{self.__get_address()}"

print("Hola")
