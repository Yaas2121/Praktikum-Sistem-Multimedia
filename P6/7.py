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