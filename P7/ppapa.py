
import cv2
import numpy as np
import matplotlib.pyplot as plt

def analisis_segmen(
    nama_video,
    waktu_awal,
    waktu_akhir
):

    video = cv2.VideoCapture(nama_video)

    fps = video.get(cv2.CAP_PROP_FPS)

    frame_awal = int(waktu_awal * fps)
    frame_akhir = int(waktu_akhir * fps)

    # Memulai pembacaan pada frame awal
    video.set(
        cv2.CAP_PROP_POS_FRAMES,
        frame_awal
    )

    frame_sebelumnya = None
    nilai_selisih = []

    indeks = frame_awal

    while indeks < frame_akhir:

        berhasil, frame = video.read()

        if not berhasil:
            break

        # Mengubah frame menjadi grayscale
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        if frame_sebelumnya is not None:

            # Menghitung selisih antar-frame
            selisih = cv2.absdiff(
                frame_sebelumnya,
                gray
            )

            rata_rata = np.mean(selisih)

            nilai_selisih.append(rata_rata)

        frame_sebelumnya = gray

        indeks += 1

    video.release()

    return nilai_selisih


# Analisis segmen statis
statis = analisis_segmen(
    "input.mp4",
    0,
    5
)

# Analisis segmen dinamis
dinamis = analisis_segmen(
    "input.mp4",
    10,
    15
)

# Menampilkan rata-rata hasil analisis
print("\nPERBANDINGAN SEGMEN VIDEO")

print(
    "Rata-rata segmen statis:",
    np.mean(statis)
)

print(
    "Rata-rata segmen dinamis:",
    np.mean(dinamis)
)

# Membuat grafik perbandingan
plt.figure(figsize=(10, 5))

plt.plot(
    statis,
    label="Segmen Statis"
)

plt.plot(
    dinamis,
    label="Segmen Dinamis"
)

plt.title("Perbandingan Redundansi Temporal")
plt.xlabel("Urutan Frame")
plt.ylabel("Rata-rata Selisih Piksel")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("hasil/perbandingan_segmen.png")
plt.show()