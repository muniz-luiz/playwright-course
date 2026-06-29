from playwright.sync_api import Page


def test_006_login_invalid(page, login_page) -> None:
    login_page.login("wrong", "wrong")
    assert "login.html" in login_page.page.url    
    login_page.assert_login_error_message()
    