from playwright.async_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.statement_button = page.locator("#viewStatementBtn")
    
    def go_to_statement(self):
        self.statement_button.click()