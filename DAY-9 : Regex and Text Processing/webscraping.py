import requests as req
from bs4 import BeautifulSoup
import pandas as pd
import os
file_name = 'result.xlsx'                        

class WebScrapping:
    """class to perform web scrapping"""

    def __init__(self, url, base_url):
        self.url = url
        self.base_url = base_url
        self.response = self.get_url(url)
        self.types = ["combo", "clump", "leaf", "plant", "pub"]
        # self.scrap()


    def get_url(self, url):
        """function to get datas from url"""
        return req.get(url)
    
    def get_headings(self, soup):
        """function to return the title heading of each prodect"""
        headings = soup.find_all('h4', class_='des-font capital title-product mb-0')
        if len(headings)>25:
            headings = headings[:25:]
        return headings

    def get_link(self, heading):
        '''function to get the url of the product'''
        return self.base_url + heading.a.get('href')
    
    def initialiseSoup(self, response):
        """returns the object of beautiful soup class"""
        return BeautifulSoup(response.content, "html.parser")

    def get_type(self, subject, dictionary):
        """returns the type of the plant"""
        for type in self.types:
            if type in subject:
                dictionary['type']= type
                break
            if len(dictionary["type"])<2:
                dictionary['type']="uncategorised"
        return dictionary['type']

    def dictionary(self):
        """return the empty dictionary to store the datas"""
        return {
            "url" : "",
            "type" : "",
            "price" : 0,
            "number" : 1,
            "variegated" : False,
            "name" : []
        }

    def get_max_page(self, soup):
        """returns the number of pages in the website"""
        return int(soup.find_all('span', class_= "page")[-1].a.get("href")[-1])

    def get_price(self, soup):
        """returns the price"""
        prices = soup.find_all('p', class_='price-product mb-0')
        if len(prices)>25:
            prices = prices[:25:]
        return prices
    
    def get_number(self, names):
        """returns the number of plants in combo"""
        return len(names)
    
    def check_variegated(self, dictionary):
        """checks if the plant is variegated or not"""
        for name in dictionary['name']:
            if "variegated" in name.lower():
                return "Variegated"   
        return "Not Variegated"
    
    def make_excel(self, dictionary):
        """makes the required excel file"""
        df = pd.DataFrame([dictionary]) 
        scores_df = df["name"].apply(pd.Series)
        scores_df.columns = [f"name_{i+1}" for i in range(scores_df.shape[1])]
        df = df.drop(columns=["name"]).join(scores_df)
        if os.path.exists(file_name):
            with pd.ExcelWriter(file_name, mode="a", if_sheet_exists="overlay", engine="openpyxl") as writer:
                df.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)
        else:
            df.to_excel(file_name, index=False)
        

    def get_name(self, soup, dictionary, subject):
        """returns the name of plants in combo along with its number"""
        plant_desc = soup.find_all("div", class_='desc product-desc')[0].ul.find_all('li')
        if dictionary["type"] == "combo":
            plant_desc = plant_desc[1].text.strip().split('-')[-1].strip().replace(";", ",").split(", ")
            if "#" not in subject:
                for name in plant_desc:
                    name = " ".join(name.split(" ")[1::])
                    if len(name)>2:
                        dictionary['name'].append(name)
            dictionary["number"]= self.get_number(dictionary["name"])              
        else:
            dictionary["name"].append(subject)
        return dictionary['name'], dictionary['number']

    def scrap(self):
        """main function that performs scrapping"""
        if self.response.status_code == 200:
            soup = self.initialiseSoup(self.response)

            #getting the number of pages in website
            max_page = self.get_max_page(soup) + 1
            for page in range(1, max_page):

                #customising the url to go to respective pages
                url = f'''https://fermosaplants.com/collections/sansevieria?page={page}'''

                #getting the data from the website
                result = self.get_url(url)
                soup = self.initialiseSoup(result)

                #getting the headings
                headings = self.get_headings(soup)

                #getting the prices
                prices = self.get_price(soup)

                #initialising the dictionary
                dictionary = self.dictionary()

                #iterating the headings one by one
                for item in range(len(headings)):
                    try:
                        #customising the url of the product
                        link = self.get_link(headings[item])
                        dictionary['url'] = link
                        dictionary['price']= prices[item].span.text.split(' ')[-1]

                        #extracting the subject from the headings for each item
                        subject = headings[item].a.text.lower()
                        dictionary['type'] = self.get_type(subject, dictionary)

                        #getting the plant information by visiting the link
                        plant_info = self.get_url(link)
                        if plant_info.status_code == 200:
                            soup = self.initialiseSoup(plant_info)

                            #getting name and number of plants
                            dictionary['name'], dictionary['number'] = self.get_name(soup, dictionary, subject)
                            dictionary['variegated'] = self.check_variegated(dictionary)

                        #dumping the data into excel 
                        print(dictionary)
                        self.make_excel(dictionary)

                        #resetting the values of dictionary 
                        dictionary = self.dictionary()
                        # break
                    except Exception:
                        dictionary = self.dictionary()
                break
        else:
            print("Connection error")

#driver code
url = "https://fermosaplants.com/collections/sansevieria"
base_url = 'https://fermosaplants.com'
scrap_obj = WebScrapping(url, base_url)