 import dlyoutube
def download_youtube_video(url, save_path="."): #url: URL ของวิดีโอ YouTube ที่จะดาวน์โหลดsave_path: ที่อยู่โฟลเดอร์ที่ใช้บันทึกวิดีโอ (ค่าดีฟอลต์คือโฟลเดอร์ปัจจุบัน ".")
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s', #'outtmpl': รูปแบบชื่อไฟล์ที่บันทึก เช่น "./ชื่อวิดีโอ.mp4"
        'format': 'best' #'format': 'best': ดาวน์โหลดวิดีโอด้วยคุณภาพดีที่สุดที่มี
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # ใช้ YoutubeDL ใน context manager (with) สร้าง object ydl สำหรับดาวน์โหลด โดยใช้ options ที่กำหนดไว้
        ydl.download([url])  #เริ่มดาวน์โหลดวิดีโอจาก YouTube โดยส่ง URL (แบบลิสต์) ให้กับ .download()
    video_url = input("Enter the YouTube video URL: ") #รับ URL วิดีโอจากผู้ใช้ผ่านทางคีย์บอร์ด
download_youtube_video(video_url, save_path=".") #เรียกใช้งานฟังก์ชัน download_youtube_video() โดยใช้ URL ที่ผู้ใช้ป้อน และบันทึกในโฟลเดอร์ปัจจุบัน
