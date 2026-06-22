import pytest
from pages.login_page import LoginPage


@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1366, "height": 768})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page

@pytest.fixture
def page_statement(page):
    page.set_viewport_size({"width": 1366, "height": 768})
    page.goto("https://leogcarvalho.github.io/simulabank/statement.html")
    return page
    

@pytest.fixture
def login_page(page):    
    return LoginPage(page)