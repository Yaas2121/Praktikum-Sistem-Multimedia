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