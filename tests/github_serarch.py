from playwright.sync_api import sync_playwright

def github_serarch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://github.com/')
        
        page.wait_for_timeout(10_000)
        page.close()
        browser.close
        
if __name__ == "__main__":
    github_serarch()
        