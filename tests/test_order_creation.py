from selenium.webdriver.common.by import By

from pages.landing_page import LandingPage


def test_landing_page(browser, base_url, zip_code):
    page = LandingPage(browser, base_url)
    page.open_page()
    page.should_be_landing_page()
    page.enter_zip_code(zip_code)
    page.click_get_estimate_button()


