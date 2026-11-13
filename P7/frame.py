
import cv2
import os

# Membuat folder penyimpanan frame
os.makedirs("hasil/frame_sampel", exist_ok=True)

# Membuka video
video = cv2.VideoCapture("input.mp4")

# Mengambil informasi video
total_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)

print("INFORMASI VIDEO")
print("Total Frame:", total_frame)
print("FPS:", fps)

# Menentukan interval ekstraksi
interval = 30
nomor_frame = 0

while True:
    berhasil, frame = video.read()

    if not berhasil:
        break

    if nomor_frame % interval == 0:
        nama_file = f"hasil/frame_sampel/frame_{nomor_frame}.jpg"
        cv2.imwrite(nama_file, frame)
        print("Frame disimpan:", nama_file)

    nomor_frame += 1

video.release()

print("Ekstraksi frame selesai.")
