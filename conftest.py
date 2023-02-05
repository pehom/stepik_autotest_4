import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='choose browser: Chrome or Firefox')
    parser.addoption('--language', action='store', default='en', help='choose lang')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        print("\nstart browser for test..")
        options = OptionsChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\nstart browser for test..")
        options = OptionsFirefox()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
