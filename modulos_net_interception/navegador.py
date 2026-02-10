from .config_stealth import stealth_mode


def criar_navegador(p):
    print("Criando navegador: ...")
    try:
        navegador = p.chromium.launch(headless=False)
        contexto = navegador.new_context(locale="pt-BR")
        pagina = contexto.new_page()            
        stealth_mode(pagina)
        print("Tudo deu certo")
        return navegador, pagina
    
    except Exception as e:
        print(f"Ocorreu um erro ao tentar criar um navegador: \n {e}")
        return None, None
        
        
def fechar_navegador(navegador, p):
    try:
        navegador.close()
        print("Navegador fechado")
    except Exception as e:
        print(f"Erro ao tentar fechar o navegador: \n {e}" )


