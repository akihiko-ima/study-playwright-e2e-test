from playwright.sync_api import Page

from tests.testcase.base.base_page import BasePage


class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def is_results_found(self) -> bool:
        content = self.page.content()
        return "No results found." not in content
