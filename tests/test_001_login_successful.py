
from pages import login_page 
from pages.login_page import LoginPage



def test_001_login_successful(page: LoginPage):        
    login_page = LoginPage(page)
    login_page.login("user1", "pass1")
    login_page.assert_successful_login()
    
    