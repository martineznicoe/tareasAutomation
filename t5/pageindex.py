class PageIndex():
    def __init__(self, my_Driver):
        self.query_top = 'search_query_top'
        self.query_button = 'submit_search'
        self.driver = my_Driver

    def search(self, item):
        self.driver.find_element_by_id(self.query_top).send_keys(item)
        self.driver.find_element_by_name(self.query_button).click()