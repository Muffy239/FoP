import json

class DuplicateNameError(Exception):
  pass

class NeighborhoodPets:
  def __init__(self):
    self._pet_dictionary = {}
#* pet dictionary = { 'pet name' : {'species' : pet_species,            
#*                                  'Owner : pet_owner}
    
  def add_pet(self,pet_name, pet_species, pet_owner):
    if pet_name.lower() in self._pet_dictionary :
      raise DuplicateNameError(f"{pet_name} has already been added.")
    self._pet_dictionary[pet_name.lower()] = {'Pet Species' : pet_species.lower(),
                                        'Owner' : pet_owner.lower()}
    
    
  def delete_pet(self, pet_name):
    if pet_name in self._pet_dictionary:
      del self._pet_dictionary[pet_name.lower()]
      
  
  def get_owner(self, pet_name):
    if pet_name in self._pet_dictionary:
      return self._pet_dictionary[pet_name.lower()]['Owner']
    
    
  def save_as_json(self, file_name):
   with open(file_name, 'w') as outfile:
     json.dump(self._pet_dictionary, outfile)
     
  
  def read_json(self, file_name):
    with open (file_name, 'r') as file:
      self._pet_dictionary = json.load(file)
      return self._pet_dictionary
  
  
  
  def get_all_species(self):
    species_set = set() #* No duplicates, Can ADD / REMOVE , IMMUTABLE
    
    for pet_name in self._pet_dictionary:
      pet_species = self._pet_dictionary[pet_name]['Pet Species']
      species_set.add(pet_species)
    return species_set
  
  
  




  
#! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  
if __name__ == "__main__":
  
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Creating Object  
  pet = NeighborhoodPets()
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Adding Pets to Dictionary  (Name, Species, Owner_Name)
  pet.add_pet("Rex", "Cat", "Adrian")
  pet.add_pet("Timmy", "Dog", "Brian")
  pet.add_pet("Lucky", "Hamster", "Brianna")
  pet.add_pet("Lucky", "Bird", "BMan")
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Printing Dictionary  

  print(pet._pet_dictionary)
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Deleting a pet form the Dictionary  
  pet.delete_pet("Lucky")
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Printing the Set(species_set) containing all the species of animals in Dict
  print(pet.get_all_species())
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Grabbing Owner of a pet by name
  print(pet.get_owner("Rex"))
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Writing dictionary to a JSON file
  pet.save_as_json("practice.json")
  
#*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Reading the JSON file we created.
  print(pet.read_json("practice.json"))

  

    


#? Concepts Learned:
#? 1. how to read from a json file and put it into a variable
#? 2. how to create a set
#? 3. how to write to a json file (w/o formatting -> AKA dump() method)
#? 4. Becoming familiar with accessing data from json files to manipulate
#? 5. Visualizing how data will be stored.

