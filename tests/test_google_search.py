from pages.google_page import GooglePage


def test_google_search(driver):

    google = GooglePage(driver)

    google.open_google()

    google.search("Selenium Python")

    assert "Selenium Python" in driver.title
