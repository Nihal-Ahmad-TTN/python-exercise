#Importing Libraries
import csv
import json
from io import StringIO

class CsvToJson:
    '''class to convert CSV file into Json'''

    def __init__(self, path):
        self.path = path
        self.output = "output.json"
        self.convert()
    
    def convert(self):
        '''function to convert CSV into json'''

        try: 
            #reading csv file from the path provided
            with open(self.path, 'r') as csvfile:

                #opening the json file in write mode
                with open(self.output, 'w') as jsonfile:

                    #creating the DictReader object
                    dictdata = csv.DictReader(csvfile, delimiter=";")

                    #iterating the dictionary datas
                    for data in dictdata:

                        #dumping the file into the the json file created
                        json.dump(data, jsonfile)
                        jsonfile.write("\n")

        except Exception as e:
            print(e)

class Jsontocsv:
    '''class to convert json file into csv'''

    def __init__(self, path):
        self.path = path
        self.output = "output.csv"
        self.convert()

    def convert(self):
        '''function to convert json into csv'''

        try:
            #reading json file from the path provided
            with open(self.path, 'r') as jsonfile:
                
                #initialising the list to store the field values
                fields = []

                #initialising the temp variable to make sure that fields and writeheader() will execute once only
                temp = 0

                #opening the target csv file in write mode
                with open(self.output, 'w') as csvfile:

                    #iterating the json file
                    for line in jsonfile:

                        #loading the data into dict form
                        data = json.loads(line)

                        #initalising the DictWriter object
                        csvwrite = csv.DictWriter(csvfile, fieldnames=fields, delimiter=',')

                        #condition to make sure fields and writeheader() get executed once
                        if temp == 0:
                            for key in data.keys():
                                fields.append(key)
                            
                            #writing headers into csv as first line
                            csvwrite.writeheader()
                            temp = 1
                        
                        #writing data into csv
                        csvwrite.writerow(data)
        except Exception as e:
            print(e)


class DictToCsv:
    '''class to convert a dict into CSV file using StringIO'''

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.convert()

    
    def convert(self):
        '''function to convert dict into CSV'''

        try:
            #initalising the StringIO object
            file = StringIO()

            #writing the keys of the dictionaries as header
            file.write(', '.join(self.dictionary.keys())+"\n")

            #writing the Values of keys in next line
            file.write(", ".join(map(str, self.dictionary.values()))+"\n")

            #setting the curser to 0 so that we can read the content
            file.seek(0)

            #reading the file
            print(file.read())
        except Exception as e:
            print(e)

#datas for testing
dictionary = { "name": "Nihal", "email": "nihal@gmail.com", "phone": "9999999999", "age": 21}
jsonfile = 'username.json'
csvfile = 'username.csv'

#Creating objects for different classes
ConvertToJson = CsvToJson(csvfile)
ConvertToCsv = Jsontocsv(jsonfile)
ConvertDictToJson = DictToCsv(dictionary)