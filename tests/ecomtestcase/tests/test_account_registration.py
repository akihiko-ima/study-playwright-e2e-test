from playwright.sync_api import Page

from tests.ecomtestcase.pages.main_page import MainPage
from tests.ecomtestcase.pages.register_page import RegisterPage
from tests.ecomtestcase.pages.register_results_page import RegisterResultsPage


def test_register_account(page: Page):
    page.goto("https://tutorialsninja.com/demo")

    main_page = MainPage(page)
    main_page.click_account_options()

    register_page = RegisterPage(page)
    register_page.input_account_information()

    register_results_page = RegisterResultsPage(page)
    result = register_results_page.is_account_created()

    assert result is True
