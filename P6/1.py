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
 raise FileNotFoundError("File gibran.jpg tidak ditemukan!")
img = Image.open(file_sumber).convert("RGB")
print("Gambar berhasil dibuka")
print("Dimensi gambar:", img.size)
print("Mode warna:", img.mode)
print("\nMEMBUAT KONVERSI WARNA")
rgb = img
grayscale = img.convert("L")
hsv = img.convert("HSV")

rgb.save(folder_hasil / "gambar_rgb.png")
grayscale.save(folder_hasil / "gambar_grayscale.png")
hsv.convert("RGB").save(folder_hasil / "gambar_hsv.png")
print("Semua hasil konversi berhasil disimpan.")

# Visualisasi perbandingan warna
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(rgb)
axes[0].set_title("RGB")
axes[1].imshow(grayscale, cmap="gray")
axes[1].set_title("Grayscale")
axes[2].imshow(hsv.convert("RGB"))
axes[2].set_title("HSV")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
fig.savefig(folder_hasil / "perbandingan_warna.png")
plt.close(fig)
print("Visualisasi perbandingan warna berhasil disimpan.")
# 3. KOMPRESI JPEG
# ==========================================
print("\nMEMULAI KOMPRESI JPEG")
for kualitas in [10, 50, 90]:
 nama_file = folder_hasil / f"jpeg_{kualitas}.jpeg"
 img.save(
 nama_file,
 format="JPEG",
 quality=kualitas
 )
 print(f"Berhasil: {nama_file.name}")
 print(f"Ukuran file: {nama_file.stat().st_size:,} byte")
# ==========================================
# 4. KOMPRESI PNG
# ==========================================
print("\nMEMULAI KOMPRESI PNG")
nama_png = folder_hasil / "gambar.png"
img.save(
 nama_png,
 format="PNG",
 optimize=True,
 compress_level=9
)
print("Berhasil:", nama_png.name)
print("Ukuran file:", nama_png.stat().st_size, "byte")
# ==========================================