from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_cart(self):
        button = self.browser.find_element(*MainPageLocators.CART_LINK)
        button.click()
