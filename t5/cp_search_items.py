import unittest
from selenium import webdriver
from pageindex import PageIndex
from pageitems import PageItems
from page_product import PageProduct

class ClothesCart (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.implicitly_wait(10)
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.productPage = PageProduct(self.driver)

    def test_addQuantity(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.click_orange_b()
        self.productPage.define_quantity('25')
        self.productPage.add_quantity(3)
        self.assertEqual(self.productPage.return_quantity(), '28')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if  __name__ == '__main__':
    unittest.main()