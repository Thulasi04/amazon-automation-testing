from playwright.sync_api import Page
def test_open_amazon(page: Page):
    page.goto("https://www.amazon.com/")
    page.locator("span[class='nav-line-2 ']").click()