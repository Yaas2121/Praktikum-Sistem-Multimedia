import json
from collections import Counter
import matplotlib.pyplot as plt
from pathlib import Path

# Menentukan lokasi folder praktikum
folder = Path(__file__).resolve().parent

# Menyiapkan folder hasil
folder_hasil = folder / "hasil"
folder_hasil.mkdir(exist_ok=True)

# Menentukan lokasi file JSON
file_json = folder / "frames.json"

# Memeriksa keberadaan file JSON
if not file_json.exists():
    print("File frames.json tidak ditemukan!")
    exit()

# Membaca file JSON dengan deteksi encoding
try:
    with open(file_json, "r", encoding="utf-8") as file:
        data = json.load(file)
except UnicodeDecodeError:
    with open(file_json, "r", encoding="utf-16") as file:
        data = json.load(file)

# Mengambil informasi frame
frames = data["frames"]

# Mengambil tipe setiap frame
tipe_frame = []

for frame in frames:
    if "pict_type" in frame:
        tipe_frame.append(frame["pict_type"])

# Menghitung jumlah tipe frame
jumlah = Counter(tipe_frame)

jumlah_I = jumlah.get("I", 0)
jumlah_P = jumlah.get("P", 0)
jumlah_B = jumlah.get("B", 0)

# Menampilkan hasil
print("DISTRIBUSI FRAME VIDEO")
print("======================")
print("Jumlah I-Frame:", jumlah_I)
print("Jumlah P-Frame:", jumlah_P)
print("Jumlah B-Frame:", jumlah_B)
print("Total Frame:", len(tipe_frame))

# Membuat grafik distribusi
label = ["I-Frame", "P-Frame", "B-Frame"]
nilai = [jumlah_I, jumlah_P, jumlah_B]

plt.figure(figsize=(8, 5))
plt.bar(label, nilai)

plt.title("Distribusi Frame I/P/B")
plt.xlabel("Tipe Frame")
plt.ylabel("Jumlah Frame")

plt.tight_layout()

# Menyimpan grafik
plt.savefig(folder_hasil / "distribusi_frame.png")

# Menampilkan grafik
plt.show()

print("Grafik berhasil disimpan di folder hasil!")

