import subprocess
from pathlib import Path

# Folder tempat skrip dan file audio berada
folder = Path(__file__).resolve().parent

# Daftar file audio sumber
daftar_file = [
    "1.wav",
    "2.wav",
    "3.wav",
    "4.wav",
    "5.wav"
]

print("=" * 45)
print("BATCH ENCODING AUDIO KE MP3 128 KBPS")
print("=" * 45)

berhasil = 0
gagal = 0

# Proses encoding setiap file audio
for nama_file in daftar_file:
    sumber = folder / nama_file
    hasil = folder / f"{sumber.stem}_128k.mp3"

    print(f"\nMemproses: {nama_file}")

    # Periksa keberadaan file sumber
    if not sumber.exists():
        print(f"Gagal: File {nama_file} tidak ditemukan")
        gagal += 1
        continue

    # Perintah FFmpeg
    perintah = [
        "ffmpeg",
        "-y",
        "-i", str(sumber),
        "-c:a", "libmp3lame",
        "-b:a", "128k",
        str(hasil)
    ]

    # Jalankan FFmpeg tanpa menampilkan log panjang
    proses = subprocess.run(
        perintah,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Periksa hasil proses encoding
    if proses.returncode == 0 and hasil.exists():
        print(f"Berhasil: {hasil.name}")
        berhasil += 1
    else:
        print(f"Gagal: {nama_file}")
        gagal += 1

# Ringkasan hasil encoding
print("\n" + "=" * 45)
print("RINGKASAN PROSES ENCODING")
print("=" * 45)
print(f"Jumlah file diproses : {berhasil + gagal}")
print(f"Berhasil             : {berhasil}")
print(f"Gagal                : {gagal}")
print("=" * 45)
