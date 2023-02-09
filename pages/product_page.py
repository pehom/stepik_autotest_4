from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_see_add_to_cart_button(self):
        assert self.is_element_present_and_visible(*ProductPageLocators.ADD_TO_CART_BUTTON), 'Add to cart button missed'

    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)

        button.click()
        # self.solve_quiz_and_get_code()

    def get_added_product_name_and_price(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED).text
        print(f'>>>>>>>>>added_product_name = {name}')
        print(f'>>>>>>>>>added_product_price = {price}')
        return {'name': name, 'price': price}

    def get_product_name_and_price(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(f'>>>>>>>>>product_name = {self.product_name}')
        print(f'>>>>>>>>>product_price = {self.product_price}')

    def success_message_is_not_located(self):
        return self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ADDED)

    def success_message_is_disappeared(self):
        return self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ADDED)



