from selenium import webdriver
import unittest
from time import sleep
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):
    """Base class of each test"""

    def setUp(self):
        """Tests condition"""
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com/')
        self.home_page = HomePage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.count = ProductsPage(self.driver)
        self.backpack = ProductsPage(self.driver)

    def testTest(self):
        pass

    def tearDown(self):
        self.driver.quit()
