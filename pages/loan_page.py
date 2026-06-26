from playwright.sync_api import Page, expect
from pages import login_page, home_page

class LoanPage:
    def __init__(self, page: Page):
        self.page = page
        self.loan_2000 = page.get_by_label("R$ 2.000,00")
        self.loan_5000 = page.get_by_label("R$ 5.000,00")
        self.loan_7000 = page.get_by_label("R$ 7.000,00")
        self.loan_9000 = page.get_by_label("R$ 9.000,00")
                
        # button/link that navigates back to the home page
        self.take_loan = page.locator("#loan-submit")
        self.back_to_home_page_button = page.get_by_role("link", name="Voltar para Home")
    
    def assert_on_loan_page(self):
        expect(self.page).to_have_url("**/loans.html")
        
    def amount_loan(self, amount):
        if amount == 2000:
            self.loan_2000.click()
        elif amount == 5000:
            self.loan_5000.click()
        elif amount == 7000:
            self.loan_7000.click()
        elif amount == 9000:
            self.loan_9000.click()
        else:
            raise ValueError ("Valor inválido")
        
    def click_submit(self, confirm=True):
        from pages.success_page import SuccessPage
        if confirm:
            self.page.once("dialog", lambda dialog: dialog.accept())
        else:
            self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.submit_button_click()
        
        if confirm:
            self.page.wait_for_url("**success.html")
            return SuccessPage(self.page)             
        
    def back_to_home_page(self):
        self.back_to_home_page_button.click()
        self.page.wait_for_load_state("networkidle")  # Espera até que a página esteja completamente carregada
        return home_page.HomePage(self.page)