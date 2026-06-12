# SumberYAML OpenClash Auto-Fast

Paket Streamlit sederhana untuk membuat YAML OpenClash/Mihomo dari subscription publik dengan filter anti-delay.

## Fitur

- Tidak memakai GitHub Action.
- Tidak perlu GitHub Token.
- 10 link subscription sudah otomatis tersedia.
- Hanya mengambil node dengan port `443`.
- Server output semua node dipaksa menjadi `104.17.3.81`.
- SNI/Host asli tetap dipertahankan agar akun tetap bisa konek.
- Link subscription dicek hidup terlebih dahulu.
- Node dicek berulang, default 3 kali.
- Hanya node delay rendah yang masuk YAML.
- Batas delay default `1500 ms` dan dikunci maksimal `1700 ms`, agar lebih rendah dari referensi:
  - Baidu Search: 1824 ms
  - NetEase Music: 2011 ms
  - GitHub: 1757 ms
- URL health check default OpenClash: `http://cp.cloudflare.com/generate_204`.
- Grup `GLOBAL` langsung memilih `⚡ AUTO-FAST` sebagai pilihan pertama.

## Cara pakai di Streamlit Cloud

1. Upload semua file ini ke root repository GitHub.
2. Buka Streamlit Cloud.
3. Pilih file utama:

```text
streamlit_app.py
```

4. Deploy.
5. Klik tombol **Proses & buat YAML anti delay**.
6. Download file:

```text
openclash_auto_fast.yaml
```

7. Import ke OpenClash/Mihomo.
8. Jalankan Health Check/Test Delay di OpenClash.

## Catatan penting

Aplikasi ini mengecek delay dari sisi server Streamlit, bukan dari router/lokasi internet kamu. Hasil terbaik tetap perlu dicek ulang di OpenClash setelah YAML diimport. Karena node berasal dari subscription publik, performa bisa berubah kapan saja.
