import datetime

def calcular_objetivo_e_dificuldade(data_inicio, ganho_hoje):
    hoje = datetime.date.today()
    dias_ativos = (hoje - data_inicio).days

    if dias_ativos < 30:
        objetivo = 50
    elif dias_ativos < 60:
        objetivo = 70
    elif dias_ativos < 365:
        objetivo = 100
    else:
        objetivo = 250

    if ganho_hoje >= objetivo:
        dificuldade = "Fácil"
    elif ganho_hoje >= objetivo * 0.7:
        dificuldade = "Médio"
    else:
        dificuldade = "Difícil"

    return objetivo, dificuldade


def gerar_relatorio_financeiro(ganho_hoje, data_inicio=datetime.date(2025, 7, 17)):
    objetivo, dificuldade = calcular_objetivo_e_dificuldade(data_inicio, ganho_hoje)
    
    relatorio = f"""
🧠 UNOSVIGINTI | Daily Report

💰 Ganho de hoje: {ganho_hoje}€
🎯 Objetivo mínimo: {objetivo}€
🔥 Nível de dificuldade: {dificuldade}

{"✅ Objetivo atingido!" if ganho_hoje >= objetivo else "⚠️ Objetivo ainda por atingir."}
"""
    return relatorio.strip()
