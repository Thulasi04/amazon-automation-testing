from playwright.sync_api import Page
def test_open_amazon(page: Page):
    page.goto("https://www.amazon.com/")
    page.locator("span[class='nav-line-2 ']").click()
    page.locator("[type='email']").type("invalidusername")
    page.locator('[type="submit"]').click()
    page.locator('[class="a-icon a-icon-close"]').click()
    page.locator('[type="email"]').click()
    page.locator('[type="email"]').type("kvz.xx777@gmail.com")
    page.locator('[type="submit"]').click()
    page.locator('[type="password"]').type("Kavya@automation")
    page.locator('[type="submit"]').click()
    page.locator('[type="text"]').type("iphone")
    page.locator('[id="nav-search-submit-button"]').click()
    page.locator('[name="submit.addToCart"]').click()
    page.locator('[type="submit"]').click()

