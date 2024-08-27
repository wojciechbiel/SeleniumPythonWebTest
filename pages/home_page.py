from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


class Locators:
    """Main website locators"""
    LOGIN_LINK = (By.ID, "login-button")


class HomePage(BasePage):
    """Main website"""
    def click_log_in(self):
        """Click Login button and go back to the login page"""
        el = self.driver.find_element(*Locators.LOGIN_LINK)
        el.click()
        return LoginPage(self.driver)
