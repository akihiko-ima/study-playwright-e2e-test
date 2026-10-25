from playwright.sync_api import Locator, Page

from tests.testcase.base.base_page import BasePage
from tests.testcase.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def input_text_box(self) -> None:
        locator: Locator = self.page.locator(MainPageLocators.TEXT_BOX)
        self.page.wait_for_timeout(5_000)
        locator.fill("unittest")

    def click_go_button(self) -> None:
        locator: Locator = self.page.locator(MainPageLocators.GO_BUTTON)
        self.page.wait_for_timeout(5_000)
        locator.click()
