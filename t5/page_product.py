class PageProduct():
    def __init__(self, my_driver):
        self.quantity = 'quantity_wanted'
        self.plus_button = '//*[@id="quantity_wanted_p"]/a[2]/span'
        self.driver = my_driver

    def define_quantity(self, item):
        self.driver.find_element_by_id(self.quantity).clear()
        self.driver.find_element_by_id(self.quantity).send_keys(item)

    def add_quantity(self):
        self.driver.find_element_by_xpath(self.plus_button).click()

    def return_quantity(self):
        return self.driver.find_element_by_id(self.quantity).get_property("value")