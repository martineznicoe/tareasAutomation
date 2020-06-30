from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex():
    def __init__(self, my_driver):
        self.query_top = (By.ID, 'search_query_top')
        self.query_button = (By.NAME, 'submit_search')
        self.driver = my_driver

    def search(self, item):
        #Necesito un web element "search_box"
        #para que aparezca tengo que esperar (tiene un tiempo máximo de 10 seg) una condición (until),
        #que espere hasta que el elemento "query_top" exista.
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.query_top))
        search_box.send_keys(item)

        # Necesito un web element "search_button"
        # para que aparezca tengo que esperar (tiene un tiempo máximo de 10 seg) una condición (until),
        # que espere hasta que el elemento "query_button" sea clickeable.
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.query_button))
        search_button.click()