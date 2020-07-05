from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageCasualDresses():
    def __init__(self, driver):
        self.dress_product = (By.PARTIAL_LINK_TEXT, 'Printed Dress')
        self.driver = driver

    def enter_dress_product(self):
        try:
            product_dress = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.dress_product))
            product_dress.click()
        except:
            print("No se encuentra 'dress_product'.")
