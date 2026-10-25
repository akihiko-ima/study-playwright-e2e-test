from playwright.sync_api import sync_playwright


def github_serarch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://github.com/")

        search_button = page.get_by_role("button", name="Search or jump to")
        search_button.click()

        search_box = page.get_by_role("combobox", name="Search or jump to")
        search_box.fill("Playwright")
        search_box.press("Enter")

        playwright_link = page.locator('a:has-text("Playwright")').first
        page.wait_for_timeout(5_000)
        playwright_link.click()

        page.wait_for_timeout(10_000)
        page.close()
        browser.close()


if __name__ == "__main__":
    github_serarch()
