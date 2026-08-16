from playwright.sync_api import Page

def test_amazon(page:Page):
    page.goto("https://www.amazon.com/")
    page.locator("//*[contains(text(),'Account & Lists')]").click() #xpath //   or   /  * - universal a div any tag name
    #auto waiting
    page.locator("[type='email']").type("Nagendran")
    page.locator("[type='submit']").click()
    page.locator("//*[contains(text(),'Invalid email ')]").is_visible()

    #Locators - Selectors
    #CSS and Xpath
    # <a id="gg" class="bb" href="www.google.com">google</a> element a p div h [key='value'] [class="bb"] []
    # attributes tag name content
    # element
    # css tag name attribute
