import json


class NobelData:

    def __init__(self):
        with open("nobels.json", "r") as infile:
            self._file_data = json.load(infile)

    # * Purpose:
    # * Returns data in the JSON File
    def search_file(self, year, category):
        year = str(year)
        category = category.lower()
        list_of_last_names = []
        for prize in self._file_data['prizes']:
            if prize['year'] == year and prize['category'] == category:
                for person in prize['laureates']:
                    list_of_last_names.append(person['surname'])
        return list_of_last_names


file_data = NobelData()


print(file_data.search_file(2022, "chemistry"))
