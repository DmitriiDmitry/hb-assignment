from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random

from conftest import thank_you_url
from pages.landing_page import LandingPage
from utils.utils import generate_random_name, generate_random_email, generate_us_phone

NEXT_BUTTON1 = (By.CSS_SELECTOR, "[data-autotest-button-button-next]")
NEXT_BUTTON2 = (By.CSS_SELECTOR, "[data-autotest-button-submit-next]")


def test_creating_order(browser, base_url, zip_code, thank_you_url):
    page = LandingPage(browser, base_url)
    page.open_page()
    page.should_be_landing_page()
    page.enter_zip_code(zip_code)
    page.click_get_estimate_button()

    # TODO: make multi-form wizard Page Object
    kitchen_cabinets_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-autotest-checkbox-updates-cabinets] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", kitchen_cabinets_option)
    kitchen_cabinets_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON1)).click()

    replace_all_cabinets_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-autotest-radio-worktype-replaceall] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", replace_all_cabinets_option)
    replace_all_cabinets_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    single_family_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-autotest-radio-propertytype-single] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", single_family_option)
    single_family_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    mobile_home_no_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-autotest-radio-internalmobilehome-no] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", mobile_home_no_option)
    mobile_home_no_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    owner_yes_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-autotest-radio-owner-yes] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", owner_yes_option)
    owner_yes_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON1)).click()

    kitchen_size_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-autotest-input-squarefeet-tel]"))
    )
    random_size = random.randint(10, 30)
    kitchen_size_field.clear()
    kitchen_size_field.send_keys(str(random_size))

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    second_budget_option = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-autotest-radio-budget-2] + label"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_budget_option)
    second_budget_option.click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    full_name_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-autotest-input-fullname-text]"))
    )
    full_name_field.clear()
    full_name_field.send_keys(generate_random_name())

    email_address_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-autotest-input-email-text]"))
    )
    email_address_field.clear()
    email_address_field.send_keys(generate_random_email())

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXT_BUTTON2)).click()

    phone_number_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-autotest-input-phonenumber-tel]"))
    )
    phone_number_field.clear()
    phone_number_field.send_keys(generate_us_phone())

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autotest-button-submit-submit-my-request]"))).click()

    try:
        WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-autotest-button-submit-phone-number-is-correct]"))).click()
    except NoSuchElementException:
        pass

    WebDriverWait(browser, 15).until(EC.url_to_be(thank_you_url))

    WebDriverWait(browser, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    thank_you_title = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h4.text-center"))
    )

    text = thank_you_title.text.strip()

    assert browser.current_url == thank_you_url
    assert thank_you_title.is_displayed()
    assert text != ""
    assert text.lower().startswith("thank you")

