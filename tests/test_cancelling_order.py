import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.landing_page import LandingPage

NEXT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-button-button-next]")


@pytest.mark.regression
def test_creating_order(browser, base_url, zip_code):
    page = LandingPage(browser, base_url)
    page.open_page()
    page.should_be_landing_page()
    page.enter_zip_code(zip_code)
    page.click_get_estimate_button()

    # TODO: make multi-form wizard Page Object
    countertops_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[data-autotest-checkbox-updates-countertop] + label")
        )
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", countertops_option)
    countertops_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autotest-button-button-no]"))
    ).click()

    WebDriverWait(browser, 15).until(EC.url_to_be(base_url))

    WebDriverWait(browser, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    landing_page = LandingPage(browser, base_url)
    landing_page.should_be_landing_page()

    assert browser.current_url == base_url, "base url does not match"
