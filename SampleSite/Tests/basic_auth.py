import unittest
from selenium import webdriver
from ../Pages/basic_page_auth import 

class BasicAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com/")
    
    def test_basic_authentication_01(self):
        """
        What does this test do?
        """
        
        main_page = page.MainPage(self.driver)