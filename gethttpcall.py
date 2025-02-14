import requests as req
import json

class getcall:
    def __init__(self, url, data={}, header='', type='get'):
        self.url = url
        self.header = header
        self.data = data
        self.type = type
        self.typecheck()
        
    def getdata(self):
        try:
            data= req.get(self.url)
            if data.status_code == 200:
                json_data= data.json()
                print(json.dumps(json_data, indent=4))
        except Exception as e:
            print(e)
    
    def typecheck(self):
        try:
            if self.type.lower() == "get":
                self.getdata()
            else:
                raise Exception
        except Exception as e:
            print(e)

while True:
    url = input("Enter The URL : ")
    type = input("Enter The Type : ")
    if url == "" or url == " ":
        url = "https://jsonplaceholder.typicode.com/posts"
    obj = getcall(url, type)
