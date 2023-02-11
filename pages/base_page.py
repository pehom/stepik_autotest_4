from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
       # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present_and_visible(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            if not element.is_displayed():
                raise ElementNotVisibleException

        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        time_start = time.time()
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f'>>>>>>is_not_element_present estimated time = {time.time()-time_start}')
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        time_start = time.time()
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print(f'>>>>>>is_disappeared estimated time = {time.time()-time_start}')
            return False

        return True

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            time.sleep(1.5)  # some delay to watch how everything is going
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                # time.sleep(1.5)  # some delay to watch how everything is going
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")
        except NoAlertPresentException:
            print('No alerts present')

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present_and_visible(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self, timeout=4):

        try:
            link = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(BasePageLocators.CART_LINK)
            )
            link.click()
        except TimeoutException:
            print(f'No cart button found')

    def should_be_authorized_user(self):
        assert self.is_element_present_and_visible(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

