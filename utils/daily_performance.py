from datetime import datetime
import json
import os

def avaliar_desempenho_diario(meta_diaria, ganhos_dia, file_path="data/daily_results.json"):
    diferenca = ganhos_dia - meta_diaria

    if diferenca >= 20:
        nivel_dificuldade = "Fácil"
    elif diferenca >= 0:
        nivel_dificuldade = "Médio"
    else:
        nivel_dificuldade = "Difícil"

    resultado = {
        "meta_diaria": meta_diaria,
        "ganhos_dia": ganhos_dia,
        "diferenca": diferenca,
        "nivel_dificuldade": nivel_dificuldade,
        "data": datetime.now().strftime("%Y-%m-%d")
    }

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            dados = json.load(f)
    else:
        dados = {}

    dados[resultado["data"]]["avaliacao"] = resultado

    with open(file_path, "w") as f:
        json.dump(dados, f, indent=4)

    return resultado
