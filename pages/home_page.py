from playwright.sync_api import Page
from pages.loan_page import LoanPage
from pages.statement_page import StatementPage
from pages.pix_page import PixPage
from pages.pay_bill import PayBillPage
from pages.login_page import LoginPage


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.statement_button = page.locator("#viewStatementBtn")
        self.pix_button = page.locator("#makePixBtn")
        self.paybill_button = page.locator("#payBillBtn")
        self.loan_button = page.locator("#loansBtn")
        self.logout_link = page.get_by_role("link", "Sair")

    
    def go_to_statement_page(self):
        self.statement_button.click()
        self.page.wait_for_url("**/statement.html")  # Espera até que a página esteja completamente carregada
        return StatementPage(self.page)    
    
    def go_to_pix_page(self):
        self.pix_button.click()
        self.page.wait_for_url("**/pix.html")  # Espera até que a página esteja completamente carregada
        return PixPage(self.page)  
        
    def go_to_paybills_page(self):
        self.paybill_button.click()
        self.page.wait_for_url("**/pay-bills.html")  # Espera até que a página esteja completamente carregada
        return PayBillPage(self.page)
    
    def go_to_loan_page(self):
        self.loan_button.click()
        self.page.wait_for_url("**/loans.html")  # Espera até que a página esteja completamente carregada
        return LoanPage(self.page)  
    
    def back_to_login(self):
        self.logout_link.click()
        self.page.wait_for_url("**/login.html")
        return LoginPage(self.page)
    
        