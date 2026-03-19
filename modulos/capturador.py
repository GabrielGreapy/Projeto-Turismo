import re



def capturar_aba_avaliacoes(pagina):
    try:
        aba_avaliar = pagina.get_by_role("tab", name = re.compile("Avaliações", re.IGNORECASE))
        
        
        if aba_avaliar.get_attribute("aria-selected") == "false":
            aba_avaliar.click()
            pagina.wait_for_timeout(2000)
        
        return aba_avaliar
    except Exception as e:
        print(f"Erro ao tentar encontrar a aba de avaliações \n {e}")
        return None



def capturar_lista_avaliacoes(pagina):
    try:
        botao_avaliar = pagina.get_by_role("button", name = re.compile("avaliar", re.IGNORECASE))
        botao_avaliar.hover()
    
    
    except Exception as e:
        print(f"Deu erro ao tentar capturar as avaliações: \n {e}")
