import BasePage

class MainPage(BasePage):
    """ HomePage action methods live here. """

    def is_title_matches(self):
        """ Verifies that the hardcoded text "___" appears in the page title."""
        return "Bleh" in self.driver.title
