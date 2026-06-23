from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.pix_page import PixPage
from pages.loan_page import LoanPage
from pages.statement_page import StatementPage
from pages.pay_bill import PayBillPage
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
    return HomePage(page)

@pytest.fixture
def statement_page(page):
    return StatementPage(page)

@pytest.fixture
def pix_page(page):    
    return PixPage(page)

@pytest.fixture
def pay_bill(page):
    return PayBillPage(page)

@pytest.fixture
def loan_page(page):    
    return LoanPage(page)



