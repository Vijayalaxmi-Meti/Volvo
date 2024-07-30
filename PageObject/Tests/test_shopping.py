import unittest
from selenium import webdriver
from PageObjectClasses.home_page import HomePage


class TestShopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.amazon.com/"
        self.home_page = HomePage(self.driver)
        
    
    def tearDown(self):
        self.driver.quit()

    def test_search_and_add_to_cart(self):
        self.home_page.open()
        search_results_page = self.home_page.search_for_product("laptop")

        if search_results_page:
            if search_results_page.click_first_product():
                print("Successfully clicked first product.")
            else:
                self.fail("Failed to click on the first product.")
        else:
            self.fail("Failed to perform search.")

if __name__ == "__main__":
    unittest.main()