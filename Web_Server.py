import os
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI
from dotenv import load_dotenv
from jinja2 import Template

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

app = FastAPI()


database = {
    'Nome_Usuario': ['Gabriel', 'Igor', 'Antony', 'Ana Jullia'],
    'Email_Usuario' : ['g@gmail.com', 'i@gmail.com', 'a@gmail.com', 'aj@gmail.com'],
    'Estrelas': [5, 1, 3, 5], 
    'Conteudo' : [
        "Lugar Maravilhoso, irei voltar", 
        "Odiei, Levei uma facada e a comida me fez mal", 
        "Fui assediado, odiei",
        "Atendimento impecável e vista linda"
    ], 
    'Local_Avaliado': ["San Picui", "San Picui", "San Picui", "Cristo Redentor"]
}


# Template HTML com Loop Jinja2
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard de Análise</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/water.css">
</head>
<body>
    <h1>📊 Analisador de Localidades</h1>
    
    <form method="post" action="/analisar_local">
        <label>Clique para julgar as reviews.</label>
        
        <button type="submit">Processar Banco de Dados</button>
    </form>
    <form method="post" action="/adicionar_ao_db">
        <label>Adicione sua propria review ao banco local</label>
        <input name="nome" placeholder ="Seu Nome"></input>
        <input name="email" type="email" placeholder="Seu Email"></input>
        <input name="estrelas" type="number" placeholder="estrelas"></input>
        <input name="conteudo" placeholder="Sua Review"></input>
        <button type="submit">Inserir</button>
    </form>

    {% if resultados %}
    <h2>Resultados:</h2>
    <table>
        <thead>
            <tr>
                <th>Usuário</th>
                <th>Emails</th>
                <th>Estrelas</th>
                <th>Conteúdo</th>
                <th>Nível de Risco (LLM)</th>
            </tr>
        </thead>
        <tbody>
            {% for r in resultados %}
            <tr>
                <td>{{ r.Nome_Usuario }}</td>
                <td< {{ r.Email_Usuario }}</td>
                <td>{{ r.Estrelas }} ⭐</td>
                <td>{{ r.Conteudo }}</td>
                <td style="font-weight: bold; color: {% if r.Nivel_risco|float < 0 %} #ff4c4c {% else %} #4caf50 {% endif %};">
                    {{ r.Nivel_risco }}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% endif %}
</body>
</html>
"""


def analisar_db(row):
    prompt = f"""
        Analise esta review da seguinte forma:
        - Pontuação da review inicial: 0
        - caso houver(-0.20) : enganação, agressão verbal, roubo, má higiene, 2 estrelas.
        - caso houver( -0.25) : assedio sexual, 1 estrela, comida ruim.
        - caso houver( -1 ) : Violencia, racismo.
        - caso houver ( +0,20 ) : 5 estrelas.
        
        Review:
        Review: {row['Estrelas']}, Conteudo: {row['Conteudo']}
        
        Calcule a pontuação final, retorne APENAS o número.
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um analista de segurança turística."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 4. Rotas do Servidor
@app.get("/", response_class=HTMLResponse)
async def home():
    return Template(html_template).render(resultados=None)

@app.post("/analisar_local", response_class=HTMLResponse)
async def analisar_local():

    
    db = pd.DataFrame(database)
    

    
    db['Nivel_risco'] = db.apply(analisar_db, axis=1)
    
    
    resultados_lista = db.to_dict(orient='records')
    db.to_csv("reviews_analisadas.csv", index=False)
    return Template(html_template).render(resultados=resultados_lista)


@app.post("/pegando_reviews", response_class=HTMLResponse)
async def pega_reviews(url_do_local):
    pass

@app.post("/adicionar_ao_db", response_class=HTMLResponse)
async def adicionar_review(POST...):
    