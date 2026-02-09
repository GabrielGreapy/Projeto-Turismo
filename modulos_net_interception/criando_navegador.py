from playwright.sync_api import sync_playwright
from config_stealth import stealth_mode

def criar_navegador():
    print("Criando navegador: ...")
    try:
        with sync_playwright as p:
            navegador = p.chromium.launch(headless=False)
            contexto = navegador.new_context()
            page = contexto.new_page()
            stealth_mode(page)
    except Exception as e:
        print(f"Ocorreu um erro ao tentar criar um navegador: \n {e}")
