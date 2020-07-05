import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_index import PageIndex
from page_dresses import PageDresses
from page_casual_dresses import PageCasualDresses
from page_dress import PageDress
import time

class BuyDress (unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.dressesPage = PageDresses(self.driver)
        self.casualDressesPage = PageCasualDresses(self.driver)
        self.dressPage = PageDress(self.driver)

    def test_buy_dress(self):
        try:
            self.indexPage.enter_dress_section()
            self.dressesPage.enter_casual_dress_category()
            self.casualDressesPage.enter_dress_product()
            self.dressPage.define_quantity(5)
            self.dressPage.define_size('L')
            self.dressPage.enter_add_cart()
            self.assertEqual('5', self.dressPage.return_quantity_cart())
            self.assertEqual('$130.00', self.dressPage.return_total_price_product())
            self.assertEqual('$2.00', self.dressPage.return_total_shipping())
            self.assertEqual('$132.00', self.dressPage.return_total_price())
            self.assertEqual('Printed Dress', self.dressPage.return_product_name())
        except:
            self.driver.save_screenshot("error_test_buy_dress.jpg")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if  __name__ == '__main__':
    unittest.main()
