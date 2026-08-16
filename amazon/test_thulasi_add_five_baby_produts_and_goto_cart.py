from playwright.sync_api import Page

def test_open_amazon(summa:Page):
    summa.goto("https://www.amazon.com/")
