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