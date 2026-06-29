from playwright.sync_api import Page



def test_006_login_invalid(login_page):
    from pages.login_page import random_string
    username = random_string()
    password = random_string()
    
    login_page.login(username, password)
    assert "login.html" in login_page.page.url
    login_page.assert_login_error_message()
    