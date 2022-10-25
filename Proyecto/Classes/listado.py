class listado():
    """"Class to enlist information from person"""
    list_of_items = {}
    __counter = 0
    def __init__(self,item):
        self.list_of_items[str(self.__counter)] = item
    def get_listado_items(self):
        for i in range(len(self.list_of_items)):
            print(f"{self.list_of_items[str(i)]}")
