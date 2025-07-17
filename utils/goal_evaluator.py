from datetime import datetime

def calcular_objetivo_e_dificuldade(data_criacao_bot: str, ganhos_dia: float):
    data_criacao = datetime.strptime(data_criacao_bot, "%Y-%m-%d")
    hoje = datetime.now()
    dias_passados = (hoje - data_criacao).days

    if dias_passados < 30:
        objetivo = 50
    elif dias_passados < 60:
        objetivo = 70
    elif dias_passados < 365:
        objetivo = 100
    else:
        objetivo = 250

    diferenca = ganhos_dia - objetivo

    if diferenca < -20:
        dificuldade = "DIFÍCIL"
    elif diferenca < 10:
        dificuldade = "MÉDIO"
    else:
        dificuldade = "FÁCIL"

    return {
        "ganhos_do_dia": ganhos_dia,
        "objetivo_diario": objetivo,
        "diferenca": diferenca,
        "dificuldade": dificuldade
    }
