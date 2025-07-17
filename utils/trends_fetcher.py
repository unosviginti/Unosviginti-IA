import random

# Lista fictícia de tópicos virais. Podes trocar por scraping ou API no futuro.
TOPICS = [
    "Como acordar às 5 da manhã e mudar a tua vida",
    "Disciplina vs Motivação",
    "Tu não precisas de ninguém para começar",
    "O silêncio é a arma dos fortes",
    "Começa agora, ou vais arrepender-te depois",
    "A tua rotina está a matar os teus sonhos",
    "Trabalha em silêncio. Deixa que os resultados falem",
    "O desconforto é o preço da liberdade",
    "Tu não és vítima, és o responsável",
    "Os teus hábitos definem o teu destino"
]

def fetch_trending_topic():
    return random.choice(TOPICS)
