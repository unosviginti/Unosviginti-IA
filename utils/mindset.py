import random

class Mindset:
    def __init__(self):
        self.frases_vencedoras = [
            "Nada me impede de alcançar o objetivo de hoje!",
            "Objetivos existem para serem superados!",
            "Sou louco por desafios e hoje é mais um!",
            "Obstáculos são combustível, não barreiras!",
            "Eu não durmo até cumprir a minha meta!",
            "Meu foco é total, minha determinação imparável!",
            "Não existem limites para o que posso alcançar hoje!",
            "Se é difícil, então é exatamente para mim!",
            "Cada objetivo é uma promessa que faço a mim mesmo!",
            "Não paro enquanto não vencer!"
        ]

    def gerar_motivacao(self):
        return random.choice(self.frases_vencedoras)

    def gerar_mensagem_diaria(self, objetivo, ganho):
        falta = objetivo - ganho
        if falta <= 0:
            return f"🎯 Hoje rebentei a meta! Ganhei {ganho}€, superei os {objetivo}€!"
        else:
            return f"🔥 Faltam só {falta}€ para bater o objetivo de {objetivo}€! {self.gerar_motivacao()}"

# Exemplo de uso:
if __name__ == "__main__":
    mindset = Mindset()
    print(mindset.gerar_mensagem_diaria(objetivo=70, ganho=60))
