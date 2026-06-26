from playwright.sync_api import Page, expect



class StatementPage:
    def __init__(self, page: Page):
        self.page = page
        self.balance = page.locator("#balance")
        self.transactions_list = page.locator("#transactions-list")
        self.back_button = page.locator("#backBtn")
        
    #transformar o R$ 5.000,00 em númerico dando replace em toda string
    def get_balance_value(self) -> float:
        text = self.balance.inner_text()
        
        value = (
            text.replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()
        )
        return float(value)
    
    def back_to_home(self):
        from pages.home_page import HomePage
        self.back_button.click()
        self.page.wait_for_url("**/home.html")
        return HomePage(self.page)
        
        