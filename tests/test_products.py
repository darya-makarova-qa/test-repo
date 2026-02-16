from playwright.sync_api import expect
def test_all_products(page):
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name = "Products").click()
    expect(page.get_by_text("All products").to_be_visible()()