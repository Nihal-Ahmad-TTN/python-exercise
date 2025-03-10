import requests
import json

class NPIData:
    """NPIData class is used to fetch the data from the npiregistry website"""
    def __init__(self,filename,jsonfilename):
          self.filename=filename
          self.jsonfilename=jsonfilename
        #   self.extractdata()
        #   pass

    def extractdata(self):
        """extractdata() is the main method of the class which fetches the data from the npiregistry website and store the data in the data.json file"""
        with open(self.filename, 'r') as file: # this is the file name where the serial numbers is strored which is used for fetching the data
            with open(self.jsonfilename, "w") as fileJson:# this is where the data is stored
                alldata=[]
                for line in file:
                    try:
                        response=requests.post("https://npiregistry.cms.hhs.gov/RegistryBack/npiDetails",json={"number":line.strip('\n"')}).json()
                            # datadict is the temporary dictionary 
                        datadict={"Number":"",
                              "Enumeration Date":"",
                              "Enumeration Type":"",
                              "Sole Proprietor":"",
                              "Satus":"",
                              "Addresses":"",
                              "Taxonomies":""
                              }
                        
                        #getting values
                        datadict["Number"]=response.get("number","")
                        datadict["Enumeration Date"]=response["basic"].get("enumerationDate", "")
                        datadict["NPI Type"]=response["enumerationType"]
                        datadict["Sole Proprietor"]=response["basic"].get("soleProprietor", "")

                        #checking if the status is active or not
                        if response["basic"]["status"]=="A":
                            datadict["Satus"]="Active"
                        else:
                            datadict["Satus"]="Inactive"

                        #datalist to store addresses
                        datalist=[]
                        for data in response["addresses"]:
                            address={"Street-1":"",
                                   "Street-2":"",
                                   "State":"",
                                    "City":"",
                                    "Pin":"",
                                    "Phone":"",
                                    "Fax":"",
                                    "Zip":""
                                }
                            address["Street-1"]=data["addressLine1"]
                            address["Street-2"]=data["addressLine2"]
                            address["State"]=data["state"]
                            address["City"]=data["city"]
                            address["Pin"]=data["postalCode"]
                            address["Phone"]=data.get("teleNumber","")
                            address["Fax"]=data.get("faxNumber","")
                            address["Zip"]=data["postalCode"]
                            datalist.append(address)
                        datadict["Addresses"]=datalist
                        datadict["Taxonomies"]=response["taxonomies"]
                        alldata.append(datadict)
                    except Exception as e:
                         pass
                 # dumping of the alldata into the data.json file(fileJson)       
                json.dump(alldata,fileJson,indent=4)        
                        
test=NPIData("num.txt","data.json")
