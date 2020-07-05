from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageDresses():
    def __init__(self, driver):
        self.casual_dresses_category = (By.LINK_TEXT, 'Casual Dresses')
        self.driver = driver

    def enter_casual_dress_category(self):
        try:
            category_casual_dresses = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.casual_dresses_category))
            category_casual_dresses.click()
        except:
            print("No se encuentra 'casual_dresses_category'.")