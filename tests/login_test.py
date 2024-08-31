from tests.base_test import BaseTest
from tests.test_data import TestData
from tests.test_data import CorrectUser


class LoginTest(BaseTest):
    """Login tests"""

    def setUp(self):
        # extending the additional setup to generate test data
        # evoking base setup
        super().setUp()
        # generate test data
        self.test_data = TestData()
        self.correct_data = CorrectUser
        self.login_page = self.home_page.click_log_in()

    def test_invalid_username(self):
        """"""
        login_page = self.home_page.click_log_in()
        # enter incorrect username
        login_page.enter_username(self.test_data.user_name)
        # enter correct password
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        # check the message about incorrect user is displayed
        self.assertEqual(""Username or password incorrect"
                         , login_page.get_error_message())

    def test_invalid_password(self):
        """Using a fake password"""
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.test_data.password)
        login_page.click_log_in()
        self.assertEqual(""Username or password incorrect"
                         , login_page.get_error_message())

    def test_invalid_username_and_password(self):
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.test_data.user_name)
        login_page.enter_password(self.test_data.password)
        login_page.click_log_in()
        self.assertEqual(""Username or password incorrect"
                         , login_page.get_error_message())

    def test_valid_username_and_password(self):
        login_page = self.home_page.click_log_in()
        login_page.enter_username(self.correct_data.correct_username)
        login_page.enter_password(self.correct_data.correct_password)
        login_page.click_log_in()
        self.products_page = self.products_page.title()
        self.assertEqual("Products", self.products_page.title())







