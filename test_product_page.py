from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', [
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #              marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
@pytest.mark.skip
class TestProductPage:
    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.get_product_name_and_price()
        page.add_product_to_cart()
        added_product = page.get_added_product_name_and_price()
        assert page.product_name == added_product['name'] and page.product_price == added_product['price'], \
            "added data doesn't match"

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        assert page.success_message_is_not_located(), 'Success message presents'

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        assert page.success_message_is_not_located(), 'Success message presents'

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        assert page.success_message_is_disappeared(), 'Success message is still presenting'

    @pytest.mark.skip
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        test_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, test_link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        test_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, test_link)
        page.open()
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        test_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, test_link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        assert basket_page.no_product_in_cart(), '>>>>>> ooops, some products in cart'
        assert basket_page.is_empty_cart_message_shown(), '>>>>>> empty cart message missed'


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'])
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, login_link)
        login_page.open()
        time.sleep(2)  # some delay to watch how everything is going
        new_email = f'goga{time.time()}@gmail.com'
        new_password = f'GOGITA{time.time()}'
        print(f'>>>>>>>>   email = {new_email}  password = {new_password}')
        login_page.register_new_user(new_email, new_password)
        time.sleep(2)  # some delay to watch how everything is going
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)  # some delay to watch how everything is going
        assert page.success_message_is_not_located(), 'Success message presents'

    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)  # some delay to watch how everything is going
        page.get_product_name_and_price()
        page.add_product_to_cart()
        added_product = page.get_added_product_name_and_price()
        assert page.product_name == added_product['name'] and page.product_price == added_product['price'], \
            "added data doesn't match"
