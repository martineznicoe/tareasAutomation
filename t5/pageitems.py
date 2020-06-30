from selenium.webdriver.common.by import By

class PageItems():
    def __init__(self, my_driver):
        self.orange_item = (By.ID, 'color_1')
        self.driver = my_driver

    def click_orange_b(self):
        self.driver.find_element(*self.orange_item).click()
