from datetime import datetime
import json
import os

def save_daily_result(amount_earned, file_path="data/daily_results.json"):
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists("data"):
        os.makedirs("data")

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            results = json.load(f)
    else:
        results = {}

    results[today] = {
        "amount_earned": amount_earned,
        "timestamp": datetime.now().isoformat()
    }

    with open(file_path, "w") as f:
        json.dump(results, f, indent=4)

    return f"✅ Ganhos de {amount_earned}€ salvos para {today}."
