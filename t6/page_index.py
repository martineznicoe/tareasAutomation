from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex():
    def __init__(self, driver):
        self.dress_button = (By.LINK_TEXT, 'DRESSES')
        self.driver = driver

    def enter_dress_section(self):
        try:
            button_dress = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.dress_button))
            button_dress.click()
        except:
            print("No se encuentra 'dress_button'.")