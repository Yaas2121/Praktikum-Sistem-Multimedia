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