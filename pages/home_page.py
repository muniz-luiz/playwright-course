from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.statement_button = page.locator("#viewStatementBtn")
        self.pix_button = page.locator("#makePixBtn")
        self.paybill_button = page.locator("#payBillBtn")
        self.loan_button = page.locator("#loansBtn")

    
    def go_to_loan_page(self):
        self.loan_button.click()
        self.page.wait_for_url("**/loans.html")