from playwright.sync_api import Page

from tests.testcase.pages.main_page import MainPage
from tests.testcase.pages.search_results_page import SearchResultsPage


def test_search_document(page: Page):
    page.goto("https://www.python.org/")

    main_page = MainPage(page)
    main_page.input_text_box()
    main_page.click_go_button()

    search_results_page = SearchResultsPage(page)
    result = search_results_page.is_results_found()

    assert result is True
