from playwright.sync_api import sync_playwright
from modulos_net_interception.navegador import criar_navegador, fechar_navegador
from modulos_net_interception.interceptador import interceptando_url


def main():
    print("Iniciando Main")
    with sync_playwright() as p:
        print("Por favor cole o link que você gostaria de pegar as informações: \n")
        url = input()
        
        
        navegador, pagina = criar_navegador(p)
        
        pagina.route("**/listreviews/**", interceptando_url)
        print("Grampo colocado")
        print("Indo ao link alvo")
        
        pagina.goto(url)
        print("Link visitado")
        
        
        
        fechar_navegador(navegador, p)

if __name__ == "__main__":
    main()
    
        
