from playwright.sync_api import Page
def test_amazon_login(page: Page):
    page.goto("https://www.amazon.com/")
    title = page.title()
    print(title)

def test_gmail_login(page):
    page.goto("https://www.gmail.com/")
    title = page.title()
    print(title)

