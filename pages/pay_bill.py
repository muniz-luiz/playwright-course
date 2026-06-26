from playwright.sync_api import Page, expect

class PayBillPage:
    def __init__(self, page: Page):
        self.page = page
        self.barcode = page.locator("#barcode")
        self.bill_amount = page.locator("#bill-amount")
        self.paybill_btn = page.get_by_role("button", name="Pagar Boleto")
        self.back_home_link = page.get_by_role("link", name="Voltar para a Home")
        
    def fill_bill(self, key : str, amount : str):
        self.barcode.fill(key)
        self.bill_amount.fill(amount)
     
    def click_pay_bill(self):
        from pages.success_page import SuccessPage
        self.paybill_btn.click()
        self.page.wait_for_url("**/success.html")
        return SuccessPage(self.page)
    
    def back_to_home(self):
        from pages.home_page import HomePage
        self.back_to_home.click()
        self.page.wait_for_url("**/home.html")
        return HomePage(self.page)
        
         
        
    