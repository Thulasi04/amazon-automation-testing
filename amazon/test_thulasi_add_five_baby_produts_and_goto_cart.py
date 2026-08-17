from playwright.sync_api import Page


def test_thulasi_add_five_baby_products_and_goto_cart(page: Page):

    # Open Amazon
    page.goto("https://www.amazon.in/")

    # Login
    page.locator("#nav-link-accountList").click()
    page.locator("input[type='email']").fill("thulasiudhaya41204@gmail.com")
    page.locator("#continue").click()
    page.locator("input[type='password']").fill("mugunthan")
    page.locator("#signInSubmit").click()

    # Search baby products
    page.locator("#twotabsearchtextbox").fill("baby products")
    page.locator("#nav-search-submit-button").click()

    # Product 1
    page.locator("[data-component-type='s-search-result'] h2 a").nth(0).click()
    page.locator("#add-to-cart-button").click()
    page.goto("https://www.amazon.in/s?k=baby+products")

    # Product 2
    page.locator("[data-component-type='s-search-result'] h2 a").nth(1).click()
    page.locator("#add-to-cart-button").click()
    page.goto("https://www.amazon.in/s?k=baby+products")

    # Product 3
    page.locator("[data-component-type='s-search-result'] h2 a").nth(2).click()
    page.locator("#add-to-cart-button").click()
    page.goto("https://www.amazon.in/s?k=baby+products")

    # Product 4
    page.locator("[data-component-type='s-search-result'] h2 a").nth(3).click()
    page.locator("#add-to-cart-button").click()
    page.goto("https://www.amazon.in/s?k=baby+products")

    # Product 5
    page.locator("[data-component-type='s-search-result'] h2 a").nth(4).click()
    page.locator("#add-to-cart-button").click()

    # Go to cart
    page.locator("#nav-cart").click()