from playwright_stealth.stealth import Stealth

def stealth_mode(page):
    try:
        stealth_obj = Stealth()
        print("Classe de stealth criada")
        try: 
            stealth_obj.use_sync(page)
        except Exception as e:
            print(" Erro ao tentar implementar o metodo stealth no navegador: \n {e}")
    except Exception as e:
        print(f"Erro ao tentar criar a classe: \n {e}")
        