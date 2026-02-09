from playwright.sync_api import sync_playwright
from modulos_net_interception.navegador import criar_navegador, fechar_navegador






def main():
    print("Iniciando Main")
    with sync_playwright() as p:
        navegador, pagina = criar_navegador(p)
        fechar_navegador(navegador, p)

if __name__ == "__main__":
    main()
    
        
