from playwright.sync_api import Page


class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.pix_key = page.locator("#pix-key")
        self.amount_input = page.locator("#pix-amount")
        self.send_pix_btn = page.get_by_role("button", name="Enviar Pix")
        self.back_to_home = page.get_by_role("link", name="Voltar para a Home")
        
    
        