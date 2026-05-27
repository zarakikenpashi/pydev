"""
Liste des fonctions qui manipulent les ressources: couche logique
"""
        
import argparse
import yt_dlp as yt

def demander_video():
    parser = argparse.ArgumentParser(description="shattube universal download")
    parser.add_argument("--url", help="lien de la ressource")
    parser.add_argument("--format", help="format de sortie: audio, vidéo")
    
    actions = ["audio", "video"]
    args = parser.parse_args()

    
    return args

def url_verified(url):
    """ Valide une url
        mauvais url = vide, sans url
    """
    if url is None:
        return False
    return True


def format_verified(formt):
    """ Valide une format """
    if not formt in ("audio","video"):
        return False
        
    return True

def is_video_url(url):
    ydl_opts = {'quiet': True, 'skip_download': True}
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
        return True
    except yt.DownloadError:
        return False

def download_video(url, conteneur):
    ydl_opts = {
        'format': format_selector,
    }
    
    if conteneur == "audio":
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{ 
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
            }]
        }

    
    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

    
    
    
def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }
    