class Pet:
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


if __name__ == "__main__":
    name = input('Name: ')
    animal_type = input('Type: ')
    age = int(input('Age: '))

    pet = Pet(name, animal_type, age)
    print('Name: ', pet.get_name(), ', Age: ', pet.get_age(), ', Type: ', pet.get_animal_type())

    pet.set_name('Mickeyy')
    print('Name: ', pet.get_name(), ', Age: ', pet.get_age(), ', Type: ', pet.get_animal_type())
