from playwright.sync_api import expect
def test_homepage_loaded(page):
    page.goto("https://automationexercise.com/")
    expect(page.get_by_role("link", name = "Products")).to_be_visible()
    