# signin_page.py
from selenium.webdriver.common.by import By
from ..pages.base_page import BasePage

class SigninPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    SIGNIN_BUTTON = (By.XPATH, "//button[@title='Sign In']")

    def enter_signin_details(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)

    def click_signin_button(self):
        self.click(self.SIGNIN_BUTTON)
