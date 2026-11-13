from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
# ==========================================
# 1. PERSIAPAN FOLDER DAN GAMBAR
# ==========================================
folder_hasil = Path("Hasil")
folder_hasil.mkdir(exist_ok=True)
file_sumber = Path("wb.jpg")
if not file_sumber.exists():
 raise FileNotFoundError("File wb.jpg tidak ditemukan!")
img = Image.open(file_sumber).convert("RGB")
print("Gambar berhasil dibuka")
print("Dimensi gambar:", img.size)
print("Mode warna:", img.mode)