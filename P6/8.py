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