import requests
import json
import threading
import time 

class NPIRegistry:
    """ 
    This class take 2 arguments:
    first argument:  must be the path of file that have all the npi ids
    second argument: must be the path of the output json file
    """

    def __init__(self, file, jsonfile):
        self.file = file
        self.jsonfile = jsonfile
        self.datas = []
        self.extract_data()

    def fetch_data(self, npi):
        """ this function accepts a single NPI number and fetch its data"""

        try:
            #customise url according to the npi id passed in argument
            url = f"https://npiregistry.cms.hhs.gov/api/?number={npi}&version=2.1"
            response = requests.get(url)
            
            #checks if there is connection error
            if response.status_code != 200:
                print(f"Failed to get data for NPI {npi}, Status Code: {response.status_code}")
                return
            
            #get the json data from the website
            data = response.json()

            #checks if the data exixts or not
            if "results" not in data:
                print(f"No data exists for NPI {npi}")
                return
            
            result = data["results"][0]

            #initialising the dictionary and inserting data
            record = {
                "Number": result.get("number", ""),
                "Enumeration Date": result.get("basic", {}).get("enumeration_date", ""),
                "NPI Type": result.get("enumeration_type", ""),
                "Sole Proprietor": result.get("basic", {}).get("sole_proprietor", ""),
                "Status": "Active" if result.get("basic", {}).get("status") == "A" else "Inactive",
                "Addresses": {
                    "Mailing Address": {},
                    "Primary Practice Address": {}
                },
                "Taxonomies": result.get("taxonomies", [])
            }
            
            #fetch the address details into a separate distionary
            for address in result.get("addresses", []):
                address_type = address.get("address_purpose", "").lower()
                address_data = {
                    "Street-1": address.get("address_1", ""),
                    "Street-2": address.get("address_2", ""),
                    "City": address.get("city", ""),
                    "State": address.get("state", ""),
                    "Zip": address.get("postal_code", ""),
                    "Phone": address.get("telephone_number", ""),
                    "Fax": address.get("fax_number", "")
                }
                
                #classifying the address into mailing and primary address
                if "mailing" in address_type:
                    record["Addresses"]["Mailing Address"] = address_data
                else:
                    record["Addresses"]["Primary Practice Address"] = address_data
            
            #appending the record of the npi id into the list
            self.datas.append(record)
            print(f"Successfully fetched data for NPI {npi}")

        
        except Exception as e:
            print(f"Error for NPI {npi}: {e}")
    
    def extract_data(self):
        """ creates thread for each npi number and execute the thread """

        #storing the npi ids into the list
        t1 = time.time()
        with open(self.file, 'r') as f:
            npi_list = [line.strip('\n"') for line in f]
        
        threads = []

        #create and execute thread for each npi id then appending it to the list
        for npi in npi_list:
            thread = threading.Thread(target=self.fetch_data, args=(npi,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        
        # Save results to JSON file
        with open(self.jsonfile, "w") as file:
            json.dump(self.datas, file, indent=5)

        t2= time.time()
        print(t2 - t1)

# Initialize the class with multi-threading
obj = NPIRegistry("number.txt", "NPIdata.json")