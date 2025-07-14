
1.def download_youtube_video(url, save_path="."): 

url: URL ของวิดีโอ YouTube ที่จะดาวน์โหลดsave_path: ที่อยู่โฟลเดอร์ที่ใช้บันทึกวิดีโอ (ค่าดีฟอลต์คือโฟลเดอร์ปัจจุบัน ".")
    
    
 2. ydl_opts = {
        2.1'outtmpl': f'{save_path}/%(title)s.%(ext)s', 
        
        #'outtmpl': รูปแบบชื่อไฟล์ที่บันทึก เช่น "./ชื่อวิดีโอ.mp4"

    2.3'format': 'best' 
        
        #'format': 'best': ดาวน์โหลดวิดีโอด้วยคุณภาพดีที่สุดที่มี
    }


     3.with yt_dlp.YoutubeDL(ydl_opts) as ydl:

    #ใช้YoutubeDLในcontextmanager(with)สร้างobjectydlสำหรับดาวน์โหลดโดยใช้option ที่กำหนดไว้

    4.ydl.download([url])

    #เริ่มดาวน์โหลดวิดีโอจาก YouTube โดยส่ง URL (แบบลิสต์) ให้กับ .download()

    5.video_url = input("Enter the YouTube video URL: ")

 #รับ URL วิดีโอจากผู้ใช้ผ่านทางคีย์บอร์ด


6.download_youtube_video(video_url, save_path=".")

#เรียกใช้งานฟังก์ชัน download_youtube_video() โดยใช้ URL ที่ผู้ใช้ป้อน และบันทึกในโฟลเดอร์ปัจจุบัน
