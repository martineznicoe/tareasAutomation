from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems():
    def __init__(self, my_driver):
        self.orange_item = (By.ID, 'color_1')
        self.order = (By.ID, 'selectProductSort')
        self.driver = my_driver

    def click_orange_b(self):
        self.driver.find_element(*self.orange_item).click()

    def select_by_text(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)
