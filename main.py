from playwright.sync_api import sync_playwright
from modulos_net_interception.navegador import criar_navegador, fechar_navegador, visitar_avaliações_googlemaps



def main():
    print("Iniciando Main")
    with sync_playwright() as p:
        print("Por favor cole o link que você gostaria de pegar as informações: \n")
        url = input()
        
        
        navegador, pagina = criar_navegador(p)
        
        
        visitar_avaliações_googlemaps(pagina, url, p)
    
        pagina.wait_for_timeout(20000)
        
        
        fechar_navegador(navegador, p)

if __name__ == "__main__":
    main()
    
        
