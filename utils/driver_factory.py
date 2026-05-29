from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    options = Options()

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    return driver
