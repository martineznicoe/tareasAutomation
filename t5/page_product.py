from selenium.webdriver.common.by import By

class PageProduct():
    def __init__(self, my_driver):
        self.quantity = (By.ID, 'quantity_wanted')
        self.plus_button = (By.XPATH, '//*[@id="quantity_wanted_p"]/a[2]/span')
        self.driver = my_driver

    def define_quantity(self, item):
        self.driver.find_element(*self.quantity).clear()
        self.driver.find_element(*self.quantity).send_keys(item)

    def add_quantity(self, item):
        for i in range(item):
            self.driver.find_element(*self.plus_button).click()

    def return_quantity(self):
        return self.driver.find_element(*self.quantity).get_property("value")