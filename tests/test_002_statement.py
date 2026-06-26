



def test_002_statement(login_page, home_page):
    login_page.login("user1", "pass1")
    login_page.assert_successful_login()
    #Vai para a pagina de extrato
    statement_page = home_page.go_to_statement_page()
    #Valida a página
    assert "statement.html" in statement_page.page.url
    #Volta para a home
    home_page = statement_page.back_to_home()
    #valida a página
    assert "home.html" in home_page.page.url
    #volta poara o Login
    back_login = home_page.back_to_login()
    #Valida a página
    assert "login.html" in login_page.page.url
    
    


