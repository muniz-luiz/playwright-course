
def test_003_make_pix(login_page, home_page) -> None:
    #vai logar na página inicial
    login_page.login("user1", "pass1")
    login_page.assert_successful_login()
    
    #Ir para statement e pegar o saldo
    statement_page = home_page.go_to_statement_page()
    balance_before = statement_page.get_balance_value()
    #Volta para o home
    home_page = statement_page.back_to_home()
    #puxar e clicar no pix
    pix_page = home_page.go_to_pix_page()
    #valida se a página vai abrir
    assert "pix.html" in pix_page.page.url
    #Digita o destino e o valor do pix
    pix_page.fill_pix("345123", "150")
    #clica no botão de envio
    success_page = pix_page.click_send_pix()
    #valida se vai para a página de sucesso
    assert "success.html" in success_page.page.url
    #voltar para o home
    home_page = success_page.back_home_btn()
    #validar se voltou
    assert "home.html" in home_page.page.url
    #click no ver extrato
    statement_page = home_page.go_to_statement_page()
    #Compara os valores
    balance_after = statement_page.get_balance_value()
    assert balance_after < balance_before
    #volta para o home
    home_page = statement_page.back_to_home()
    back_login = home_page.back_to_login()
    
    
    
    
    
    
    