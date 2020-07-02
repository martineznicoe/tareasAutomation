import unittest
from selenium import webdriver
from pageindex import PageIndex
from pageitems import PageItems
from page_product import PageProduct
import time
from selenium.webdriver.chrome.options import Options

class ClothesCart (unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        option.add_argument("incognito")
        option.add_argument("--headless")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options = option)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(10)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.productPage = PageProduct(self.driver)

    #@unittest.skip("Not need now")
    def test_addQuantity(self):
        try:
            self.indexPage.search('t-shirt')
            self.itemsPage.click_orange_b()
            self.productPage.define_quantity('25')
            self.productPage.add_quantity(3)
            self.assertEqual(self.productPage.return_quantity(), '25')
        except:
            self.driver.save_screenshot("error.jpg")

    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: A to Z')
        self.itemsPage.select_by_value('reference:asc')
        self.itemsPage.select_by_index(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if  __name__ == '__main__':
    unittest.main()