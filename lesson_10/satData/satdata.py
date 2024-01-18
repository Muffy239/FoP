import json


class SatData:
    def __init__(self, json_file):
        with open(json_file, "r") as file:
            all_data = json.load(file)
            formatted_sat_data = {}  # *{DBN : FORMATTED ROW}
            for row in all_data['data']:
                formatted_row = ", ".join([row[8], row[9], ("" if str(row[10]) == None else str(row[10])), ("" if str(row[11]) == None else str(
                    row[11])), ("" if str(row[12]) == None else str(row[12])), ("" if str(row[13]) == None else str(row[13]))])
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
