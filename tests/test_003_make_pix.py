from playwright.sync_api import Page

def test_003_make_pix(login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    