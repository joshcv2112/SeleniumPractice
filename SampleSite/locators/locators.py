from selenium.webdriver.common.by import By

"""
Types of locators in By:
CLASS_NAME
CSS_SELECTOR
ID
LINK_TEXT
NAME
PARTIAL_LINK_TEXT
TAG_NAME
XPATH
"""

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    DONATE_BUTTON = (By.CLASS_NAME, 'donate-button')
