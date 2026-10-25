from playwright.sync_api import Locator, Page

from tests.ecomtestcase.base.base_page import BasePage
from tests.ecomtestcase.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def click_account_options(self) -> None:
        # account options
        locator: Locator = self.page.locator(MainPageLocators.ACCOUNT_OPTIONS)
        self.page.wait_for_timeout(2000)
        locator.click()

        # register
        locator = self.page.locator(MainPageLocators.REGISTER)
        # actions hover
        self.page.wait_for_timeout(2_000)
        locator.hover()
        self.page.wait_for_timeout(2_000)
        locator.click()
