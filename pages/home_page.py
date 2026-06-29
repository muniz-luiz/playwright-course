from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.statement_button = page.locator("#viewStatementBtn")
        self.pix_button = page.locator("#makePixBtn")
        self.paybill_button = page.locator("#payBillsBtn")
        self.loan_button = page.locator("#loansBtn")
        self.logout_link = page.get_by_role("link", name="Sair")

    
    def go_to_statement_page(self):
        from pages.statement_page import StatementPage
        expect(self.statement_button).to_be_visible()
        with self.page.expect_navigation(url="**/statement.html"):  # Espera até que a página statement esteja completamente carregada
            self.statement_button.click()
        return StatementPage(self.page)    
    
    def go_to_pix_page(self):
        from pages.pix_page import PixPage
        expect(self.pix_button).to_be_visible()
        with self.page.expect_navigation(url="**/pix.html"):  # Espera até que a página pix esteja completamente carregada
            self.pix_button.click()
        return PixPage(self.page) 
        
    def go_to_paybills_page(self):
        from pages.pay_bill import PayBillPage
        expect(self.paybill_button).to_be_visible()
        with self.page.expect_navigation(url="**/pay-bills.html"):  # Espera até que a página pagar boletos esteja completamente carregada
            self.paybill_button.click()
        return PayBillPage(self.page)
    
    def go_to_loan_page(self):
        from pages.loan_page import LoanPage
        expect(self.loan_button).to_be_visible()
        with self.page.expect_navigation(url="**/loans.html"): # Espera até que a página pagar loans esteja completamente carregada
            self.loan_button.click()
        return LoanPage(self.page)  
    
    def back_to_login(self):
        from pages.login_page import LoginPage
        self.logout_link.click()
        self.page.wait_for_url("**/login.html")
        return LoginPage(self.page)
    
        