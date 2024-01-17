import json


class SatData:
<<<<<<< HEAD
    #! Purpose: Takes in a file and loads the information to the "file_data" variable
    #* This reads the given json file thrown into the class object EX: sat_data = satData(sat.json).
    #* Json.load is loading the given file's data to the "file_data" variable.
    #* We use a for loop to iterate over all rows listed held in the "data" key of the given object in the json file.
    #* From there we target which elements(indexes) we want to pull from the "data" key and append them to the formatted_file_data variable. (Utilize .JOIN() METHOD TO ACCOMPLISH THIS)
    #! .JOIN METHOD: creates a string (EX: ", ".join(["this", "is", "cool"]) ==> this, is , cool) separating all items in a list by a comma & space.
    #* by targeting the index 8 & 9 : we pull the DBN and SCHOOL NAME from the list.
    #* Next we target the Number of Test Takers(Index: 10), Critical Reading Mean (Index: 11), Mathematics Mean(Index: 12), and Writing Mean(Index: 13) from the list.
    #* we utilize a comprehensive if statement to return "NONE" if there is no information provided for that category.
    #?  (return this )
    def __init__(self, json_file):
        with open(json_file, 'r') as file:
            file_data = json.load(file)
            formatted_file_data = {}  #? { DBN : formatted string }
            for listed_row in file_data['data']:
                formatted_row = ", ".join([listed_row[8], listed_row[9], ("" if str(listed_row[10]) == None else str(listed_row[10])), 
                                                                                ("" if str(listed_row[11]) == None else str(listed_row[11])),
                                                                                ("" if str(listed_row[12]) == None else str(listed_row[12])),
                                                                                ("" if str(listed_row[13]) == None else str(listed_row[13]))])
                formatted_file_data[listed_row[8]] = formatted_row
            self._data = formatted_file_data
            
    
    def save_as_csv(self, dbn_list):
        with open("dbn.csv", "w") as outfile:
            outfile.write(f"DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean \n")
            for dbn_key in dbn_list:
                if dbn_key in self._data:
                    formatted_row = self._data[dbn_key]
                    outfile.write(f"{formatted_row}\n")
        return


sd = SatData('sat.json') 
dbns = ["02M303", "02M294", "01M450", "02M418"] 
sd.save_as_csv(dbns)
=======
    def __init__(self, json_file):
        with open(json_file, "r") as file:
            all_data = json.load(file)
            formatted_sat_data = {}
            for row in all_data['data']:
                formatted_row = ", ".join([row[8], row[9], ("" if str(row[10]) == None else str(row[10])),
                                           ("" if str(row[11]) ==
                                            None else str(row[11])),
                                           ("" if str(row[12]) ==
                                            None else str(row[12])),
                                           ("" if str(row[13]) == None else str(row[13]))])
                formatted_sat_data[row[8]] = formatted_row
            self._data = formatted_sat_data

    def save_as_csv(self, dbn_list):
        with open('dbn.csv', 'w') as outfile:
            outfile.write(
                'DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean' + '\n')
            for dbn in dbn_list:
                if dbn in self._data:
                    outfile.write(self._data[dbn] + '\n')
        return


sd = SatData('sat.json')
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
>>>>>>> 2a1007f2a1daed17946f4097857351455824ea19
