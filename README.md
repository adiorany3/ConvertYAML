# SumberYAML OpenClash Anti Delay

Aplikasi Streamlit sederhana untuk membuat YAML OpenClash/Mihomo dari subscription publik dengan filter cepat dan stabil.

## Fitur

- Tidak memakai GitHub Action.
- Link subscription bawaan sudah dimasukkan.
- Hanya mengambil node port `443`.
- Output `server` dipaksa menjadi `104.17.3.81`.
- Domain asli tetap dipakai sebagai `SNI`/`Host` agar kompatibilitas tetap lebih baik.
- Link mati otomatis diabaikan.
- Node dites berulang agar yang masuk bukan sekadar hidup, tetapi lebih stabil.
- Node lambat dibuang berdasarkan batas delay.
- YAML OpenClash memakai grup:
  - `🚀 PROXY`
  - `⚡ AUTO-FAST` (`url-test`)
  - `🛟 FALLBACK`
  - `🔁 LOAD-BALANCE`
- Mengaktifkan opsi Mihomo/OpenClash yang membantu respons:
  - `unified-delay: true`
  - `tcp-concurrent: true`
  - `global-client-fingerprint: chrome`
  - DNS fake-ip

## Cara pakai di Streamlit Cloud

1. Upload isi folder ini ke repository GitHub baru.
2. Buka Streamlit Cloud.
3. Pilih file utama:

```text
streamlit_app.py
```

4. Deploy.
5. Klik tombol **Proses & buat YAML anti delay**.
6. Download `openclash_anti_delay.yaml`.
7. Import YAML ke OpenClash.
8. Jalankan **Health Check / Test Delay** di OpenClash.

## Pengaturan yang disarankan

- Maksimal node tercepat: `30`
- Maks delay masuk YAML: `900 ms`
- Tes ulang per node: `3`
- Minimal sukses: `2`
- Timeout node: `2.5 detik`
- Interval url-test OpenClash: `60 detik`
- Toleransi auto-switch: `25 ms`

## Catatan

Aplikasi ini memilih node yang cepat berdasarkan koneksi TCP ke server asli port 443 dan mengurutkan berdasarkan skor stabilitas. Karena sumbernya subscription publik, kualitas akun bisa berubah sewaktu-waktu. Untuk hasil terbaik, jalankan ulang proses ketika koneksi mulai lambat.
