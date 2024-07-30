from selenium.webdriver.common.by import By
from PageObjectClasses.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.result_links = (By.CSS_SELECTOR, "div.s-result-item h2 a")

    
    def click_first_product(self):
        try:
            self.click_element(self.result_links)
            return True
        except Exception as e:
            print(f"Exception occurred while clicking product: {str(e)}")
            return False