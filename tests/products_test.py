from tests.base_test import BaseTest
from tests.test_data import CorrectUser
from time import sleep


class ProductsTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.correct_data = CorrectUser
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        self.count = self.products_page.add_product()

    def test_counting_items(self):
        """Test counting the number of items in the cart"""

        self.navbar_click = self.products_page.navbar_click()
        self.reset = self.products_page.reset()
        self.driver.refresh()
        self.count = self.products_page.add_product()
        self.assertEqual('6', self.products_page.produckts_number())

    def test_correct_backpack(self):
        self.first_name = self.products_page.backpack_first_name()
        self.first_price = self.products_page.backpack_first_price()
        self.backpack = self.products_page.backpack()
        self.second_name = self.products_page.backpack_second_name()
        self.second_price = self.products_page.backpack_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_correct_light(self):
        self.first_name = self.products_page.light_first_name()
        self.first_price = self.products_page.light_first_price()
        self.light = self.products_page.light()
        self.second_name = self.products_page.light_second_name()
        self.second_price = self.products_page.light_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_correct_tshirt(self):
        self.first_name = self.products_page.tshirt_first_name()
        self.first_price = self.products_page.tshirt_first_price()
        self.tshirt = self.products_page.tshirt()
        self.second_name = self.products_page.tshirt_second_name()
        self.second_price = self.products_page.tshirt_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_correct_jacket(self):
        self.first_name = self.products_page.jacket_first_name()
        self.first_price = self.products_page.jacket_first_price()
        self.jacket = self.products_page.jacket()
        self.second_name = self.products_page.jacket_second_name()
        self.second_price = self.products_page.jacket_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_correct_onesie(self):
        self.first_name = self.products_page.onesie_first_name()
        self.first_price = self.products_page.onesie_first_price()
        self.onesie = self.products_page.onesie()
        self.second_name = self.products_page.onesie_second_name()
        self.second_price = self.products_page.onesie_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_correct_tshirt_red(self):
        self.first_name = self.products_page.tshirt_red_first_name()
        self.first_price = self.products_page.tshirt_red_first_price()
        self.tshirt_red = self.products_page.tshirt_red()
        self.second_name = self.products_page.tshirt_red_second_name()
        self.second_price = self.products_page.tshirt_red_second_price()
        self.assertEqual(self.first_name, self.second_name)
        self.assertEqual(self.first_price, self.second_price)

    def test_navbar_roll(self):
        """Checking navbar extention"""
        self.navbar_click = self.products_page.navbar_click()
        self.aria_hidden = self.products_page.aria_hidden()
        self.assertEqual("false", self.aria_hidden)

    def test_all_item(self):
        self.navbar_click = self.products_page.navbar_click()
        self.all_item = self.products_page.all_item()
        self.assertEqual("Products", self.products_page.title())

    def test_about(self):
        self.navbar_click = self.products_page.navbar_click()
        self.about = self.products_page.about()
        self.assertEqual('Test it all. Free', self.products_page.about_title())

    def test_log(self):
        self.navbar_click = self.products_page.navbar_click()
        self.logout = self.products_page.logout()
        self.assertEqual('Swag Labs', self.products_page.start_page())

    def test_reset(self):
        self.navbar_click = self.products_page.navbar_click()
        self.reset = self.products_page.reset()
        self.assertEqual("Products", self.products_page.title())
