import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_index import PageIndex
from page_signin import PageSignIn
from page_authentication import PageAuthentication

class Login (unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.signinPage = PageSignIn(self.driver)
        self.authenticationPage = PageAuthentication(self.driver)

    def test_case_1_login(self):
        try:
            self.indexPage.enter_sign_in_button()
            self.signinPage.complete_textbox_email('hola-gmail.com.ar')
            self.signinPage.complete_textbox_pass('12345')
            self.signinPage.enter_signin_button()
            self.assertIn('Invalid email', self.authenticationPage.return_error_text())
        except:
            self.driver.save_screenshot("error_test_case_1_login.jpg")

    def test_case_2_login(self):
        try:
            self.indexPage.enter_sign_in_button()
            self.signinPage.complete_textbox_email('martineznicoe@gmail.com.ar')
            self.signinPage.complete_textbox_pass('12345')
            self.signinPage.enter_signin_button()
            self.assertIn('Authentication failed', self.authenticationPage.return_error_text())
        except:
            self.driver.save_screenshot("error_test_case_2_login.jpg")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if  __name__ == '__main__':
    unittest.main()