from pages.google_page import GooglePage


def test_google_search(driver):

    google = GooglePage(driver)

    google.open_google()

    google.search("Selenium")

    assert "Selenium" in driver.title
