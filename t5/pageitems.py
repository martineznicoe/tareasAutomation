class PageItems():
    def __init__(self, my_driver):
        self.orange_item = 'color_1'
        self.driver = my_driver

    def click_orange_b(self):
        self.driver.find_element_by_id(self.orange_item).click()
