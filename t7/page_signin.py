from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageSignIn():
    def __init__(self, driver):
        self.textbox_email = (By.ID, 'email')
        self.textbox_pass = (By.ID, 'passwd')
        self.signin_button = (By.ID, 'SubmitLogin')
        self.driver = driver

    def complete_textbox_email(self, item):
        try:
            email_textbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.textbox_email))
            email_textbox.send_keys(item)
        except:
            print("No se encuentra 'textbox_email'.")

    def complete_textbox_pass(self, item):
        try:
            pass_textbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.textbox_pass))
            pass_textbox.send_keys(item)
        except:
            print("No se encuentra 'textbox_pass'.")

    def enter_signin_button(self):
        try:
            button_signin = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.signin_button))
            button_signin.click()
        except:
            print("No se encuentra 'signin_button'.")