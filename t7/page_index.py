from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex():
    def __init__(self, driver):
        self.sign_in_button = (By.LINK_TEXT, 'Sign in')
        self.driver = driver

    def enter_sign_in_button(self):
        try:
            button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sign_in_button))
            button_sign_in.click()
        except:
            print("No se encuentra 'sign_in_button'.")