from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.loan_page import LoanPage




def test_004_loan(page: Page, login_page: LoginPage, home_page: HomePage) -> None:
    login_page.login("user1", "pass1")
    #valido se fui para home page
    assert "home.html" in page.url
    #agora eu clico no emprestimo
    home_page.go_to_loan_page()
    #valido se estou na pagina de emprestimo
    assert "loans.html" in page.url
    #clica no back to home 
    loan_page = LoanPage(page)
    home_page = loan_page.back_to_home_page()
    assert "home.html" in page.url
    
    
    
