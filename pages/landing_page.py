from pages.base_page import BasePage
from pages.locators import LandingPageLocators


class LandingPage(BasePage):
    def should_be_landing_page(self):
        self.should_be_zip_code_field()
        self.should_be_get_estimate_button()

    def should_be_zip_code_field(self):
        assert self.is_element_present(*LandingPageLocators.FIRST_ZIP_CODE_FIELD), (
            "First zip code field is not present"
        )

    def should_be_get_estimate_button(self):
        assert self.is_element_present(*LandingPageLocators.FIRST_GET_ESTIMATE_BUTTON), (
            "First Get Estimate Button is not present"
        )

    def enter_zip_code(self, zip_code):
        zip_input = self.browser.find_element(*LandingPageLocators.FIRST_ZIP_CODE_FIELD)
        zip_input.clear()
        zip_input.send_keys(zip_code)

    def click_get_estimate_button(self):
        get_estimate_button = self.browser.find_element(
            *LandingPageLocators.FIRST_GET_ESTIMATE_BUTTON
        )
        get_estimate_button.click()
