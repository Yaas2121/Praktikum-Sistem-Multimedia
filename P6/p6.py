from PIL import Image
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.metrics import (
 peak_signal_noise_ratio,
 structural_similarity
)
# 1. MEMBUAT FOLDER HASIL
folder_hasil = Path("Hasil")
folder_hasil.mkdir(exist_ok=True)
# 2. MEMBUKA GAMBAR ASLI
file_sumber = Path("wb.jpg")
img_asli = Image.open(file_sumber).convert("RGB")
array_asli = np.array(img_asli)
print("Gambar berhasil dibuka")
print("Dimensi gambar:", img_asli.size)
print("Mode warna:", img_asli.mode)
print("Bentuk array:", array_asli.shape)
# 3. FUNGSI MENGHITUNG MSE
def hitung_mse(gambar_asli, gambar_kompresi):
 selisih = (
 gambar_asli.astype(np.float64) -
 gambar_kompresi.astype(np.float64)
 )
 mse = np.mean(selisih ** 2)
 return mse
# 4. FUNGSI MENGHITUNG PSNR MANUAL
def hitung_psnr_manual(mse):
 if mse == 0:
  return float('inf')
 psnr = 10 * math.log10((255.0 ** 2) / mse)
 return psnr
# 5. DAFTAR FILE JPEG
daftar_jpeg = {
 "JPEG 10": "jpeg_10.jpeg",
 "JPEG 50": "jpeg_50.jpeg",
 "JPEG 90": "jpeg_90.jpeg"
}
# 6. PERHITUNGAN MSE DAN PSNR MANUAL
print("\nPERHITUNGAN MSE DAN PSNR MANUAL")
for nama, nama_file in daftar_jpeg.items():
 file_kompresi = folder_hasil / nama_file
 img_kompresi = Image.open(file_kompresi).convert("RGB")
 array_kompresi = np.array(img_kompresi)
 if array_asli.shape != array_kompresi.shape:
  raise ValueError(f"Dimensi gambar tidak sama: {nama_file}")
 mse = hitung_mse(array_asli, array_kompresi)
 psnr = hitung_psnr_manual(mse)
 print(f"\n{nama}")
 print(f"MSE : {mse:.4f}")
 print(f"PSNR : {psnr:.2f} dB")
# 7. PERBANDINGAN PSNR MANUAL DAN SCIKIT-IMAGE
print("\nPERBANDINGAN PSNR MANUAL DAN SCIKIT-IMAGE")
for nama, nama_file in daftar_jpeg.items():
 file_kompresi = folder_hasil / nama_file
 img_kompresi = Image.open(file_kompresi).convert("RGB")
 array_kompresi = np.array(img_kompresi)
 mse = hitung_mse(array_asli, array_kompresi)
 psnr_manual = hitung_psnr_manual(mse)
 psnr_skimage = peak_signal_noise_ratio(
 array_asli,
 array_kompresi,
 data_range=255
 )
 print(f"\n{nama}")
 print(f"PSNR Manual : {psnr_manual:.2f} dB")
 print(f"PSNR Skimage : {psnr_skimage:.2f} dB")
# 8. PERHITUNGAN SSIM
print("\nPERHITUNGAN SSIM")
for nama, nama_file in daftar_jpeg.items():
 file_kompresi = folder_hasil / nama_file
 img_kompresi = Image.open(file_kompresi).convert("RGB")
 array_kompresi = np.array(img_kompresi)
 ssim = structural_similarity(
 array_asli,
 array_kompresi,
 channel_axis=2,
 data_range=255
 )
 print(f"\n{nama}")
 print(f"SSIM : {ssim:.4f}")
# 9. DAFTAR GAMBAR JPEG DAN WEBP
daftar_file = {
 "JPEG 10": "jpeg_10.jpeg",
 "JPEG 50": "jpeg_50.jpeg",
 "JPEG 90": "jpeg_90.jpeg",
 "WebP 10": "webp_10.webp",
 "WebP 50": "webp_50.webp",
 "WebP 90": "webp_90.webp"
}
# 10. PERBANDINGAN JPEG DAN WEBP
print("\nPERBANDINGAN JPEG DAN WEBP")
data_hasil = []
for nama, nama_file in daftar_file.items():
 file_kompresi = folder_hasil / nama_file
 img_kompresi = Image.open(file_kompresi).convert("RGB")
 array_kompresi = np.array(img_kompresi)
 if array_asli.shape != array_kompresi.shape:
  raise ValueError(f"Dimensi gambar tidak sama: {nama_file}")
 mse = hitung_mse(array_asli, array_kompresi)
 psnr = hitung_psnr_manual(mse)
 ssim = structural_similarity(
 array_asli,
 array_kompresi,
 channel_axis=2,
 data_range=255
 )
 ukuran_file = file_kompresi.stat().st_size
 data_hasil.append({
 "nama": nama,
 "ukuran": ukuran_file,
 "psnr": psnr,
 "ssim": ssim
 })
# 11. MENAMPILKAN TABEL HASIL
print("\nTABEL PERBANDINGAN JPEG DAN WEBP")
print("-" * 75)
print(
 f"{'Format':<15} "
 f"{'Ukuran (byte)':>15} "
 f"{'PSNR (dB)':>15} "
 f"{'SSIM':>12}"
)
print("-" * 75)
for data in data_hasil:
 print(
 f"{data['nama']:<15} "
 f"{data['ukuran']:>15} "
 f"{data['psnr']:>15.2f} "
 f"{data['ssim']:>12.4f}"
 )
print("-" * 75)
# 12. GRAFIK PSNR TERHADAP UKURAN FILE
plt.figure(figsize=(9, 5))
for format_gambar in ["JPEG", "WebP"]:
 data_format = [
 d for d in data_hasil
 if d["nama"].startswith(format_gambar)
 ]
 plt.plot(
 [d["ukuran"] / 1024 for d in data_format],
 [d["psnr"] for d in data_format],
 marker="o",
 label=format_gambar
 )
plt.title("Perbandingan PSNR terhadap Ukuran File")
plt.xlabel("Ukuran File (KB)")
plt.ylabel("PSNR (dB)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(folder_hasil / "grafik_psnr.png")
plt.close()
print("\nGrafik PSNR berhasil disimpan.")
# 13. GRAFIK SSIM TERHADAP UKURAN FILE
plt.figure(figsize=(9, 5))
for format_gambar in ["JPEG", "WebP"]:
 data_format = [
 d for d in data_hasil
 if d["nama"].startswith(format_gambar)
 ]
 plt.plot(
 [d["ukuran"] / 1024 for d in data_format],
 [d["ssim"] for d in data_format],
 marker="o",
 label=format_gambar
 )
plt.title("Perbandingan SSIM terhadap Ukuran File")
plt.xlabel("Ukuran File (KB)")
plt.ylabel("SSIM")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(folder_hasil / "grafik_ssim.png")
plt.close()
print("Grafik SSIM berhasil disimpan.")
print("\nSEMUA PROSES BERHASIL DISELESAIKAN!")