import dlyoutube
def download_youtube_video(url, save_path="."):
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s', "
        'format': 'best' #'format': 'best': 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
        ydl.download([url]) 
    video_url = input("Enter the YouTube video URL: ") 
download_youtube_video(video_url, save_path=".")
