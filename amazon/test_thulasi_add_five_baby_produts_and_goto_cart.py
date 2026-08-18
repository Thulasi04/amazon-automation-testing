from playwright.sync_api import Page

def test_thulasi(page: Page):

#login
    page.goto("https://www.amazon.in/")
    #page.locator("[id='nav-link-accountList']").click()
    #page.locator("[type = 'email']").type("thulasiudhaya41204@gmail.com")
    #page.locator("[class='a-button-input']").click()

    #page.locator("[type = 'password']").type("mugunthan")
    #page.locator("[class='a-button-input']").click()

#all
    page.locator("i[class='hm-icon nav-sprite']").click()
    page.locator("[data-ref-tag='nav_em_1_1_1_12']").click()
    page.locator("[href='/gp/browse.html?node=1571274031&ref_=nav_em_sbc_tbk_baby_products_0_2_15_3']").click()

#1stproduct
    page.locator("[data-testid='add-to-cart-button']").click()
    page.locator("[data-testid='add-to-cart-variational-modal-button']").click()
