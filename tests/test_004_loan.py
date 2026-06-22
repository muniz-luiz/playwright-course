from playwright.sync_api import Page, expect
from pages import login_page, home_page, loan_page


def test_004_loan(page, login_page, home_page) -> None:
    login_page.login("user1", "pass1")
    #valido se fui para home page
    assert "home.html" in page.url
    #agora eu clico no emprestimo
    home_page.go_to_loan_page()
    #valido se estou na pagina de emprestimo
    assert "loans.html" in page.url
    
    
    
