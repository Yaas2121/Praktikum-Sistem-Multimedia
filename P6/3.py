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