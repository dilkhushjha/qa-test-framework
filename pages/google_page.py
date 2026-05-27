from selenium.webdriver.common.by import By


class GooglePage:

    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver

    def open_google(self):
        self.driver.get("https://www.google.com")

    def search(self, text):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(text + "\n")
