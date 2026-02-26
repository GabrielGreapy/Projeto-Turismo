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
