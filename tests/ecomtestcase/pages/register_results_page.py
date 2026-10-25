from playwright.sync_api import Page

from tests.ecomtestcase.base.base_page import BasePage


class RegisterResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_account_created(self) -> bool:
        content = self.page.content()
        result = "Your Account Has Been Created!" in content
        self.page.wait_for_timeout(2000)
        return result
