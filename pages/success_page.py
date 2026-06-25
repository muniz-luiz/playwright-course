from playwright.sync_api import Page


class SuccessPage:
    def __init__(self, page:Page):
        self.page = page
        self.success_btn = page.locator("#backHomeBtn")        
        
    def back_home_btn(self):
        from pages.home_page import HomePage
        self.success_btn.click()
        self.page.wait_for_url("**/home.html")
        return HomePage(self.page)
        