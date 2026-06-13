# SumberYAML OpenClash No Check

Versi Streamlit Online sederhana untuk mengambil akun langsung dari:

```text
https://github.com/adiorany3/SumberYAML/raw/refs/heads/main/input/links.txt
```

## Fitur

- Tidak melakukan cek alive/delay akun di Streamlit.
- Akun dari `input/links.txt` dianggap sudah hidup.
- Tetap membuang akun yang tidak lengkap agar YAML OpenClash tidak error.
- Tetap membuang duplikat.
- Nama akun otomatis diganti menjadi aman: `AKUN-001-VLESS`, `AKUN-002-TROJAN`, dan seterusnya.
- Hanya akun port `443`.
- Server output dipaksa ke `104.17.3.81`.
- SNI/Host/path asli akun tetap dipertahankan.
- GLOBAL langsung memilih `AUTO-FAST`.
- Rule kategori: Social Media, YouTube, Edukasi, Streaming.
- Rule block iklan/tracker/hijacking/malware berbasis rule-provider.

## Cara pakai di Streamlit Cloud

1. Upload semua file ke GitHub.
2. Deploy ke Streamlit Cloud.
3. Main file: `streamlit_app.py`.
4. Klik **Proses & buat YAML tanpa cek akun**.
5. Download `openclash_sumberyaml_no_check.yaml`.

## Catatan

Aplikasi tidak mengecek akun karena sumber dianggap sudah hidup. Validasi koneksi penuh tetap dilakukan oleh OpenClash/Mihomo melalui health check `AUTO-FAST` setelah YAML dipakai.
