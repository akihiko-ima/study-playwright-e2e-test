from playwright.sync_api import Locator, Page

from tests.ecomtestcase.base.base_page import BasePage
from tests.ecomtestcase.locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def input_account_information(self) -> None:
        # first name
        locator: Locator = self.page.locator(RegisterPageLocators.FIRST_NAME)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("test_first_name")
        self.page.wait_for_timeout(1000)

        # last name
        locator = self.page.locator(RegisterPageLocators.LAST_NAME)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("test_last_name")
        self.page.wait_for_timeout(1000)

        # email
        locator = self.page.locator(RegisterPageLocators.EMAIL)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("test@unittestt202610251101.com")
        self.page.wait_for_timeout(1000)

        # telephone
        locator = self.page.locator(RegisterPageLocators.TELEPHONE)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("012345678")
        self.page.wait_for_timeout(1000)

        # password
        locator = self.page.locator(RegisterPageLocators.PASSWORD)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("P@ssw0rd")
        self.page.wait_for_timeout(1000)

        # password confirm
        locator = self.page.locator(RegisterPageLocators.PASSWORD_CONFIRM)
        locator.click()
        self.page.wait_for_timeout(1000)
        locator.fill("P@ssw0rd")
        self.page.wait_for_timeout(1000)

        # newsletter
        locator = self.page.locator(RegisterPageLocators.NEWSLETTER)
        locator.click()
        self.page.wait_for_timeout(1000)

        # privacy policy
        locator = self.page.locator(RegisterPageLocators.PRIVACY_POLICY)
        locator.click()
        self.page.wait_for_timeout(1000)

        # click on the continue button
        locator = self.page.locator(RegisterPageLocators.CONTINUE_BUTTON)
        locator.click()
        self.page.wait_for_timeout(2000)
