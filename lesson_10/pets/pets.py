import json


class DuplicateNameError(Exception):
    pass


class Pet:
    def __init__(self, name, species, owner):
        self._name = name
        self._species = species
        self._owner = owner


class NeighborhoodPets:
    def __init__(self):
        self._pet_dictionary = {}
        # *                      {'Pet Name' : { 'Species' : pet_species,
        # *                                      'Owner' : Pet_owner }}

    def add_pet(self, pet_name, pet_species, pet_owner):
        if pet_name in self._pet_dictionary:
            raise DuplicateNameError(f"{pet_name} is already added.")
        self._pet_dictionary[pet_name] = {
            'Pet Species': pet_species, 'Owner': pet_owner}

    def delete_pet(self, pet_name):
        if pet_name in self._pet_dictionary:
            del self._pet_dictionary[pet_name]
        else:
            print(f"{pet_name} is not found in the dictionary.")

    def get_owner(self, pet_name):
        if pet_name in self._pet_dictionary:
            return self._pet_dictionary[pet_name]['Owner']


pet = NeighborhoodPets()

pet.add_pet("Ted", "Cat", "adrian")
pet.add_pet("Brian", "Dog", "Daniel")
pet.add_pet("Ian", "Snake", "Sarah")


print(pet._pet_dictionary)

print(pet.get_owner("Ted"))
