from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):

    def is_empty_cart_message_shown(self):
        try:
            message_element = self.browser.find_element(*BasketPageLocators.CART_MESSAGE)
            if message_element:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def should_be_no_product_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_PRODUCT), '>>>>>> ooops, some products in cart'

    def should_be_empty_cart_message(self):
        assert self.is_empty_cart_message_shown(), '>>>>>> empty cart message missed'
