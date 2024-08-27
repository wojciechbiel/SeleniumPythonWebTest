from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Locators:
    """Login page locators"""
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOG_IN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By. XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')


class LoginPage(BasePage):
    def enter_username(self, username):
        """Entering username"""
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        """Entering password"""
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el.send_keys(password)

    def click_log_in(self):
        "Clicking the Login button"
        self.driver.find_element(*Locators.LOG_IN_BTN).click()

    def get_error_message(self):
        """Error waiting and then Error message return"""
        wait = WebDriverWait(self.driver, 4)
        error_msg = self.driver.find_element(*Locators.ERROR_MSG)
        return error_msg.text







