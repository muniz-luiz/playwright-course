from playwright.sync_api import Page, expect
from pages import login_page, home_page

class LoanPage:
    def __init__(self, page: Page):
        self.page = page
        # button/link that navigates back to the home page
        self.back_to_home_page_button = page.get_by_role("link", name="Voltar para Home")
    
    def assert_on_loan_page(self):
        expect(self.page).to_have_url("**/loans.html")
        
    def back_to_home_page(self):
        self.back_to_home_page_button.click()
        self.page.wait_for_load_state("networkidle")  # Espera até que a página esteja completamente carregada
        return home_page.HomePage(self.page)