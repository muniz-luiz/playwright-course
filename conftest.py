from pages.login_page import LoginPage
import pytest


BASE_URL = "https://leogcarvalho.github.io/simulabank/login.html"

@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1380, "height": 768})
    page.goto(BASE_URL)
    return page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    from pages.home_page import HomePage
    return HomePage(page)

@pytest.fixture
def loan_page(page):
    from pages.loan_page import LoanPage
    return LoanPage(page)