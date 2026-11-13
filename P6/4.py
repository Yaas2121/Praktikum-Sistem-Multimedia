#4. KOMPRESI WEBP
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