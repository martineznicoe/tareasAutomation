from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class PageDress():
    def __init__(self, driver):
        self.quantity = (By.ID, 'quantity_wanted')
        self.size = (By.ID, 'group_1')
        self.add_cart_button = (By.NAME, 'Submit')
        self.layer_quantity_cart = (By.CLASS_NAME, 'ajax_cart_quantity')
        self.total_price_product = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[1]/span')
        self.total_shipping = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[2]/span')
        self.total_price = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[3]/span')
        self.product_name = (By.ID, 'layer_cart_product_title')
        self.driver = driver


    def define_quantity(self, item):
        try:
            quantity_number = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.quantity))
            quantity_number.clear()
            quantity_number.send_keys(item)
        except:
            print("No se encuentra 'quantity'.")

    def define_size(self, item):
        try:
            size_select = Select(WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.size)))
            size_select.select_by_visible_text(item)
        except:
            print("No se encuentra 'size'.")

    def enter_add_cart(self):
        try:
            button_add_cart = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_cart_button))
            button_add_cart.click()
        except:
            print("No se encuentra 'add_cart_button'.")

    def return_quantity_cart(self):
        try:
            cart_cuantity_layer = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.layer_quantity_cart))
            return cart_cuantity_layer.text
        except:
            print("No se encuentra 'layer_quantity_cart'.")

    def return_total_price_product(self):
        try:
            product_price_total = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.total_price_product))
            return product_price_total.text
        except:
            print("No se encuentra 'total_price_product'.")

    def return_total_shipping(self):
        try:
            shipping_total = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.total_shipping))
            return shipping_total.text
        except:
            print("No se encuentra 'total_shipping'.")

    def return_total_price(self):
        try:
            price_total = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.total_price))
            return price_total.text
        except:
            print("No se encuentra 'total_price'.")

    def return_product_name(self):
        try:
            name_product = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.product_name))
            return name_product.text
        except:
            print("No se encuentra 'product_name'.")