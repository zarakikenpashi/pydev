"""
    shattube: outil cli pour telecharger
    des medias sur plateformes publiques
"""
import utils_ytdlp as yt

if __name__== "__main__":
    ytb = yt.demander_video()
    if not yt.url_verified(ytb.url):
        print("Echec lors du téléchargement, veuillez renseigner l'url de la vidéo")
    elif not yt.format_verified(ytb.format):
        print(f"Echec lors du téléchargement, le format '{ytb.format}' n'est pas supporté")
    elif not yt.is_video_url(ytb.url):
        print("Video unavailable")
    else:
        yt.download_video(ytb.url, ytb.format)

    
    
    
    