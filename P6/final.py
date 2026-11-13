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
 raise FileNotFoundError(f"File sumber tidak ditemukan: {file_sumber}")
ukuran_file_asli = file_sumber.stat().st_size
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

# 5. KOMPRESI WEBP
# ==========================================
print("\nMEMULAI KOMPRESI WEBP")
for kualitas in [10, 50, 90]:
 nama_file = folder_hasil / f"webp_{kualitas}.webp"
 img.save(
 nama_file,
 format="WEBP",
 quality=kualitas
 )
 print(f"Berhasil: {nama_file.name}")
 print(f"Ukuran file: {nama_file.stat().st_size:,} byte")
# ==========================================
# 6. TABEL PERBANDINGAN KOMPRESI
# ==========================================
print("\nTABEL PERBANDINGAN HASIL KOMPRESI")
print("-" * 65)
print(
 f"{'Format':<12}"
 f"{'Kualitas':<15}"
 f"{'Ukuran (byte)':>18}"
)
print("-" * 65)
data_kompresi = [
 ("PNG", "-", nama_png)
]
for kualitas in [10, 50, 90]:
 data_kompresi.append((
 "JPEG",
 str(kualitas),
 folder_hasil / f"jpeg_{kualitas}.jpeg"
 ))
 data_kompresi.append((
 "WebP",
 str(kualitas),
 folder_hasil / f"webp_{kualitas}.webp"
 ))
for format_gambar, kualitas, file in data_kompresi:
 ukuran = file.stat().st_size
 print(
 f"{format_gambar:<12}"
 f"{kualitas:<15}"
 f"{ukuran:>18,}"
 )
print("-" * 65)
# ==========================================
# 7. HISTOGRAM RGB
# ==========================================
print("\nMEMBUAT HISTOGRAM RGB")
warna = ["red", "green", "blue"]
fig, ax = plt.subplots(figsize=(10, 5))
for i, nama_warna in enumerate(warna):
 kanal = img.getchannel(i)
 histogram = kanal.histogram()
 ax.plot(
 histogram,
 color=nama_warna,
 label=nama_warna
 )
ax.set_title("Histogram RGB Gambar Asli")
ax.set_xlabel("Nilai Intensitas Piksel")
ax.set_ylabel("Jumlah Piksel")
ax.legend()
plt.tight_layout()
fig.savefig(folder_hasil / "histogram_rgb.png")
plt.close(fig)
print("Histogram RGB berhasil disimpan.")
# 8. HISTOGRAM GRAYSCALE
# ==========================================
print("\nMEMBUAT HISTOGRAM GRAYSCALE")
histogram_gray = grayscale.histogram()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(histogram_gray, color="gray")
ax.set_title("Histogram Grayscale Gambar Asli")
ax.set_xlabel("Nilai Intensitas Piksel")
ax.set_ylabel("Jumlah Piksel")
plt.tight_layout()
fig.savefig(folder_hasil / "histogram_grayscale.png")
plt.close(fig)
print("Histogram Grayscale berhasil disimpan.")

# 9. PERBANDINGAN HISTOGRAM KOMPRESI
# ==========================================
print("\nMEMBANDINGKAN HISTOGRAM KOMPRESI")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
 grayscale.histogram(),
 label="Gambar Asli"
)
for nama in ["jpeg_10.jpeg", "webp_10.webp"]:
 file = folder_hasil / nama
 gambar_kompresi = Image.open(file).convert("L")
 ax.plot(
 gambar_kompresi.histogram(),
 label=nama
 )
ax.set_title("Perbandingan Histogram Sebelum dan Sesudah Kompresi")
ax.set_xlabel("Nilai Intensitas Piksel")
ax.set_ylabel("Jumlah Piksel")
ax.legend()
plt.tight_layout()
fig.savefig(folder_hasil / "perbandingan_histogram_kompresi.png")
plt.close(fig)
print("Perbandingan histogram berhasil disimpan.")
# ==========================================
# 10. ANALISIS EFEK RESIZING
# ==========================================
print("\nMEMULAI ANALISIS RESIZING")
print("Dimensi asli:", img.size)
print("Ukuran file asli:", ukuran_file_asli, "byte")
persentase_resize = [50, 25, 10]
for persentase in persentase_resize:
 lebar = max(1, int(img.width * persentase / 100))
 tinggi = max(1, int(img.height * persentase / 100))
 hasil_resize = img.resize(
 (lebar, tinggi),
 Image.Resampling.LANCZOS
 )
 nama_file = folder_hasil / f"resize_{persentase}.jpg"
 hasil_resize.save(
 nama_file,
 format="JPEG",
 quality=90
 )
 ukuran = nama_file.stat().st_size
 print(f"\nResize {persentase}%")
 print(f"Dimensi: {lebar} x {tinggi}")
 print(f"Ukuran file: {ukuran:,} byte")
print("\nProses resizing selesai.")
# ==========================================

# 11. VISUALISASI PERBANDINGAN RESIZING
# ==========================================
fig, axes = plt.subplots(1, 4, figsize=(16, 6))
axes[0].imshow(img)
axes[0].set_title("Gambar Asli")
for ax, persentase in zip(axes[1:], persentase_resize):
 nama_file = folder_hasil / f"resize_{persentase}.jpg"
 gambar = Image.open(nama_file)
 ax.imshow(gambar)
 ax.set_title(f"Resize {persentase}%")
for ax in axes:
 ax.axis("off")
plt.tight_layout()
fig.savefig(folder_hasil / "perbandingan_resizing.png")
plt.close(fig)
print("Visualisasi resizing berhasil disimpan.")
# ==========================================
# 12. TABEL HASIL RESIZING
# ==========================================
print("\nTABEL HASIL RESIZING")
print("-" * 65)
print(
 f"{'File':<22}"
 f"{'Dimensi':<22}"
 f"{'Ukuran (byte)':>18}"
)
print("-" * 65)
print(
 f"{'wb.jpg':<22}"
 f"{str(img.width) + ' x ' + str(img.height):<22}"
 f"{ukuran_file_asli:>18,}"
)
for persentase in persentase_resize:
 nama_file = folder_hasil / f"resize_{persentase}.jpg"
 gambar = Image.open(nama_file)
 ukuran = nama_file.stat().st_size
 dimensi = f"{gambar.width} x {gambar.height}"
 print(
 f"{nama_file.name:<22}"
 f"{dimensi:<22}"
 f"{ukuran:>18,}"
 )
print("-" * 65)
print("\nSEMUA PROSES PENGOLAHAN GAMBAR SELESAI.")