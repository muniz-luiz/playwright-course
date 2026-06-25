from playwright.sync_api import Page

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.pix_key = page.locator("#pix-key")
        self.amount_input = page.locator("#pix-amount")
        self.send_pix_btn = page.get_by_role("button", name="Enviar Pix")
        self.back_to_home = page.get_by_role("link", name="Voltar para a Home")
        
    def fill_pix(self, key : str, amount : str):
        self.pix_key.fill(key)
        self.amount_input.fill(amount)
    
    def click_send_pix(self):
        from pages.success_page import SuccessPage
        self.send_pix_btn.click()
        self.page.wait_for_url("**/success.html")
        return SuccessPage(self.page)
        
    def click_back_home(self):
        from pages.home_page import HomePage
        self.back_to_home.click()
        self.page.wait_for_url("**/home.html")
        return HomePage(self.page)
        
        