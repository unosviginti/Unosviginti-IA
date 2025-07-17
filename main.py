import os
import time
from utils.voice_generator import generate_voice
from utils.video_generator import generate_video
from utils.caption_generator import generate_captions
from utils.trends_fetcher import fetch_trending_topic

def run_bot():
    while True:
        topic = fetch_trending_topic()
        print(f"📈 Tópico do momento: {topic}")

        voice_path = generate_voice(topic)
        print(f"🔊 Voz gerada: {voice_path}")

        video_path = generate_video(voice_path)
        print(f"🎥 Vídeo gerado: {video_path}")

        generate_captions(video_path, topic)
        print("✅ Legendas adicionadas")

        print("🚀 Vídeo pronto para publicação!")
        time.sleep(3600)  # Espera 1h antes do próximo

if __name__ == "__main__":
    run_bot()
