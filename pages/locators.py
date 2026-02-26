from selenium.webdriver.common.by import By


class LandingPageLocators:
    FIRST_ZIP_CODE_FIELD = (By.ID, "zipCode")
    FIRST_GET_ESTIMATE_BUTTON = (By.CSS_SELECTOR, "button[data-autotest-button-submit-0]")
