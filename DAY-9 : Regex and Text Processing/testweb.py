import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from webscraping import WebScrapping 

class TestWebScrapping(unittest.TestCase):
    """class to test the units"""

    def setUp(self):
        """settling up the url and blase url for each test cases"""
        self.url = "https://fermosaplants.com/collections/sansevieria"
        self.base_url = "https://fermosaplants.com"
        self.scraper = WebScrapping(self.url, self.base_url)


    @patch('webscraping.req.get')
    def test_get_url_success(self, mock_get):
        '''testing the success of get_url() method'''
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        response = self.scraper.get_url(self.url)
        self.assertEqual(response.status_code, 200)
    

    @patch('webscraping.req.get')
    def test_get_url_failure(self, mock_get):
        '''testing the failure of get_url() method'''
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        response = self.scraper.get_url(self.url)
        self.assertEqual(response.status_code, 404)


    def test_get_type(self):
        '''testing the get_type() method'''
        dictionary = {'type': ''}
        subject = "beautiful combo"
        result = self.scraper.get_type(subject, dictionary)
        self.assertEqual(result, "combo")


    def test_get_number(self):
        '''testing the failure of get_number() method'''
        names = ["Plant A", "Plant B", "Plant C"]
        count = self.scraper.get_number(names)
        self.assertEqual(count, 3)


    def test_get_price(self):
        '''testing the failure of get_price() method'''
        html = """
        <html>
            <body>
                <p class='price-product mb-0'><span>Rs. 999.00</span></p>
                <p class='price-product mb-0'><span>Rs. 499.00</span></p>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        prices = self.scraper.get_price(soup)
        self.assertEqual(len(prices), 2)
        self.assertIn('Rs. 999', prices[0].text)


    def test_check_variegated(self):
        '''testing the failure of check_varigated() method'''
        dictionary = {'name': ["Variegated Snake Plant", "Golden Hahnii"]}
        result = self.scraper.check_variegated(dictionary)
        self.assertEqual(result, "Variegated")
        
        dictionary = {'name': ["Snake Plant", "Golden Hahnii"]}
        result = self.scraper.check_variegated(dictionary)
        self.assertEqual(result, "Not Variegated")


    def test_dictionary_initialization(self):
        '''testing the dictionary() method'''
        expected_dict = {
            "url": "",
            "type": "",
            "price": 0,
            "number": 1,
            "variegated": False,
            "name": []
        }
        self.assertEqual(self.scraper.dictionary(), expected_dict)


    def test_get_headings(self):
        """'''testing the get_heading method'''"""
        html = """
        <html>
            <body>
                <h4 class='des-font capital title-product mb-0'>
                    <a href='/product1'>Product 1</a>
                </h4>
                <h4 class='des-font capital title-product mb-0'>
                    <a href='/product2'>Product 2</a>
                </h4>
            </body>
        </html>
        """
        soup = BeautifulSoup(html, "html.parser")
        headings = self.scraper.get_headings(soup)
        self.assertEqual(len(headings), 2)
        self.assertIn('Product 1', headings[0].text)

    
if __name__ == '__main__':
    unittest.main()
