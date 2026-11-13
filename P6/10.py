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