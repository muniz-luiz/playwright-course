from playwright.sync_api import Page

def test_001_login_successful(page, login_page) -> None:
    login_page.login("user1", "pass1")
    login_page.assert_successful_login()
    
    
    #clicar no botão sair para voltar para a tela de login
    login_page.logout()
   
    
    