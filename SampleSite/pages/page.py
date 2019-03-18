#import elements.element
from elements.element import BasePageElement
from locators.locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """ This class gets the search text from the specified Locator. """
    locator = 'q'

class BasePage(object):
    """ Base class to initialize the base page that will be called from all pages. """

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """ Home page action methods come here. """

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """ Verifies that the hardcoded text "Python" appears in page title. """
        return "The Internet" in self.driver.title

    def click_go_button(self):
        """ Triggers the search. """
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_donate_button(self):
        element = self.driver.find_element(*MainPageLocators.DONATE_BUTTON)
        element.click()



class SearchResultsPage(BasePage):
    """ Search results page action methods come here. """

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
