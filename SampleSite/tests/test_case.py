import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pages.page
import unittest
from selenium import webdriver

import time

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://the-internet.herokuapp.com")

    def test_search_in_python_org(self):
        main_page = pages.page.MainPage(self.driver)
        time.sleep(10)
        assert main_page.is_title_matches(), "the-internet.herokuapp.com title doesn't match."
        #Sets the text of search textbox to "pycon"
        #main_page.search_text_element = "pycon"
        #main_page.click_go_button()
        #search_results_page = pages.page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        #assert search_results_page.is_results_found(), "No results found."

    # def test_donate_button(self):
    #     main_page = page.MainPage(self.driver)
    #     main_page.click_donate_button()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
