from playwright.sync_api import Page, expect

def random_string(lenght = 6):
        import random
        import string
        return ''.join(random.choices(string.ascii_lowercase, k=lenght))


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Entrar")        

        
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def logout(self):
        self.page.get_by_role("link", name="Sair").click()
        expect(self.page).to_have_url("https://leogcarvalho.github.io/simulabank/login.html")
    
    def assert_successful_login(self):
        expect(self.page).to_have_url("https://leogcarvalho.github.io/simulabank/home.html")
        
    def assert_login_error_message(self):
        expect(self.page.locator("#error-message"))
        
    
        
        
    
        