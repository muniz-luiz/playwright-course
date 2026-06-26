from playwright.sync_api import Page

def test_004_pay_bill(home_page, login_page):
    #Vai fazer o login
    login_page.login("user1", "pass1")
    login_page.assert_successful_login()
    assert "home.html" in home_page.page.url
    
    #Pegar o saldo inicialmente
    statement_page = home_page.go_to_statement_page()
    balance_before = statement_page.get_balance_value()
    home_page = statement_page.back_to_home()
    
    #Clica no botão de boleto
    pay_bill = home_page.go_to_paybills_page()
    assert "pay-bills.html" in pay_bill.page.url
    
    #Preenche os dados
    pay_bill.fill_bill("456879", "400")
    success_page = pay_bill.click_pay_bill()
    assert "success.html" in success_page.page.url
    home_page = success_page.back_home_btn()
    assert "home.html" in home_page.page.url
    
    #Vai para o extrato e valida o valor
    statement_page = home_page.go_to_statement_page()
    assert "statement.html" in statement_page.page.url
    balance_after = statement_page.get_balance_value()
    assert balance_after < balance_before
    home_page = statement_page.back_to_home()
    assert "home.html" in home_page.page.url
    back_login = home_page.back_to_login()
    
    
    
    
    
    
    
    
    
    
    
    
    
