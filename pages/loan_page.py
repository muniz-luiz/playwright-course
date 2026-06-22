from playwright.sync_api import Page, expect
from pages import login_page, home_page

class LoanPage:
    def __init__(self, page: Page):
        self.page = page
    
    def assert_on_loan_page(self):
        expect(self.page).to_have_url("**/loans.html")