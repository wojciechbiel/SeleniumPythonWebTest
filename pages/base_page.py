from selenium.webdriver.common.alert import Alert


class BasePage:
    """Page Base Class"""
    def __init__(self, driver):
        """Browser driver capture"""
        self.driver = driver
        self.alert = Alert(self.driver)
