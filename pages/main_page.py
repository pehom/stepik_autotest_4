from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *pargs, **kwargs):
        super(MainPage, self).__init__(*pargs, **kwargs)


