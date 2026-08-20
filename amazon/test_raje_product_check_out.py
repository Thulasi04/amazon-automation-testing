from playwright.sync_api import Page
def test_raje_product_check_out(page:Page):
    page.goto("https://www.amazon.in/")
    page.locator("[class='nav-line-2 ']").click()
    page.locator("[type='email']").type("9962087300")
    page.locator("[type='submit']").click()
    page.locator("[type='password']").type("Eleven")
    page.locator("[id='signInSubmit']").click()
    page.locator("[class='hm-icon nav-sprite']").click()
    page.locator("[href='/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2']").click()
    page.locator("[href='/gp/bestsellers/home-improvement/ref=zg_bs_home-improvement_sm']").click()
    page.locator(
        "[src='https://images-eu.ssl-images-amazon.com/images/I/51CEc354bZL._AC_UL675_SR675,480_.jpg']").click()
    page.locator(
        "[src='https://images-eu.ssl-images-amazon.com/images/I/51CEc354bZL._AC_UL900_SR900,600_.jpg']").click()
    page.locator("[class='_cDEzb_p13n-sc-css-line-clamp-3_g3dy1']").click()
    page.locator("[class='a-section a-spacing-mini _cDEzb_noop_3Xbw5']").click()
    page.locator("[alt='Happi Planet Magic Eraser | Pack of 4 | No Scratch Multi-Surface Cleaning Sponge | Removes 100+ Tough Stains | Just Add Water | Walls, Kitchen, Bathroom, Shoes & Switch Boards']").click()
    page.locator("[id='buy-now-button']").click()
    page.locator("[id='pp-mtECJB-118']").click()
    page.locator("[id='pp-mtECJB-121']").click()
    page.locator("[type='tel']").type("5123756783456784")
    page.locator("[id='pp-O3NprG-21_2']").click()
    page.locator("[fdprocessedid='vt6cx']").click()
    page.locator("[id='pp-PElz9F-149']").type("222")
    page.locator("[fdprocessedid='3hlzrc']").click()














