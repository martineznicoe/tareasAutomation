from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class PageDresses():
    def __init__(self, driver):
        self.casual_dresses_category = (By.LINK_TEXT, 'Casual Dresses')
        self.product_sort = (By.ID, 'selectProductSort')
        self.list_view = (By.XPATH, '//*[@id="list"]/a')
        self.add_cart_button = (By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[2]/a[1]')
        self.driver = driver

    def enter_casual_dress_category(self):
        try:
            category_casual_dresses = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.casual_dresses_category))
            category_casual_dresses.click()
        except:
            print("No se encuentra 'casual_dresses_category'.")

    def select_product_sort(self, item):
        try:
            select_sort_product = Select(WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.product_sort)))
            select_sort_product.select_by_visible_text(item)
        except:
            print("No se encuentra 'product_sort'.")

    def enter_list_view(self):
        try:
            view_list = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.list_view))
            view_list.click()
        except:
            print("No se encuentra 'list_view'.")

    def enter_add_cart_button(self):
        try:
            button_add_cart = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_cart_button))
            button_add_cart.click()
        except:
            print("No se encuentra 'add_cart_button'.")


