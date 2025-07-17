from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def generate_captions(video_path, text):
    # Carrega o vídeo original
    video = VideoFileClip(video_path)

    # Cria o clip de texto (legenda)
    caption = TextClip(
        text,
        fontsize=70,
        color='white',
        size=(video.w * 0.9, None),
        method='caption',
        align='center',
        font='Arial-Bold'
    ).set_duration(video.duration).set_position(("center", "bottom"))

    # Junta o vídeo com as legendas
    final_video = CompositeVideoClip([video, caption])

    # Define caminho de saída com legenda
    captioned_path = "output/video_with_captions.mp4"
    final_video.write_videofile(captioned_path, fps=24)

    return captioned_path
