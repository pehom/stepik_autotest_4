from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    PRODUCT_PRICE_ADDED = (By.CSS_SELECTOR, 'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    CART_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    CART_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    CART_PRODUCT = (By.CSS_SELECTOR, '#basket_formset > div > div')
