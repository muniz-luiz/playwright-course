
def test_003_make_pix(login_page, home_page) -> None:
    #vai logar na página inicial
    login_page.login("user1", "pass1")
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
    
    
    
    
    