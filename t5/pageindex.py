from selenium.webdriver.common.by import By

class PageIndex():
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver

    def search(self, item):
        self.driver.find_element(*self.query_top).send_keys(item)
        self.driver.find_element(*self.query_button).click()