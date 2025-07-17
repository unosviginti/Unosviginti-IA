from elevenlabs import generate, save, set_api_key

set_api_key("TUA_API_KEY_AQUI")

def generate_voice(text):
    audio = generate(
        text=text,
        voice="Josh",  # Podes trocar por outra voz disponível
        model="eleven_multilingual_v2"
    )
    file_path = "output/audio.mp3"
    save(audio, file_path)
    return file_path
