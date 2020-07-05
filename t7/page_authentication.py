from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageAuthentication():
    def __init__(self, driver):
        self.error_text = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')
        self.driver = driver

    def return_error_text(self):
        try:
            text_error = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_text))
            return text_error.text
        except:
            print("No se encuentra 'error_text'.")