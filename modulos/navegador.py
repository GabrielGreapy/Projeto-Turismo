from .config_stealth import stealth_mode
from .capturador import capturar_aba_avaliacoes

def criar_navegador(p):
    print("Criando navegador: ...")
    try:
        navegador = p.chromium.launch(headless=False)
        contexto = navegador.new_context(locale="pt-BR",
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
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
        
        
def visitar_avaliações_googlemaps( pagina, url, p):
    for i in range(2):
        pagina.wait_for_timeout(2000)
        pagina.goto(url)
    print("Reload feito")
    aba_avaliacoes = capturar_aba_avaliacoes(pagina)
    
    
    


