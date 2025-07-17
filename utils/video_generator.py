from moviepy.editor import AudioFileClip, ColorClip, CompositeVideoClip

def generate_video(voice_path):
    # Carrega o áudio gerado
    audio = AudioFileClip(voice_path)

    # Cria um vídeo com fundo preto da mesma duração do áudio
    video = ColorClip(size=(720, 1280), color=(0, 0, 0), duration=audio.duration)

    # Junta o vídeo com o áudio
    final_video = CompositeVideoClip([video.set_audio(audio)])

    # Define caminho de saída
    video_path = "output/final_video.mp4"
    final_video.write_videofile(video_path, fps=24)

    return video_path
