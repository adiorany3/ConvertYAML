# Patch Notes - GLOBAL No DIRECT

Perubahan:

- Menghapus `DIRECT` dari selector `GLOBAL` di semua YAML output.
- Mempertahankan `DIRECT` untuk rule lokal/LAN/private agar akses router dan perangkat lokal tetap normal.
- Memperbarui generator (`sumberyaml_core.py`, `streamlit_app.py`, dan lite builder di `generate_yaml.py`) agar hasil generate ulang tetap tidak memasukkan `DIRECT` ke selector `GLOBAL`.
- `PROXY` dan group lain masih dapat memiliki `DIRECT` jika dibutuhkan, tetapi `GLOBAL` tidak.

Tujuan:

- Mencegah koneksi jatuh ke `DIRECT` setelah OpenClash reload.
- Memastikan default route tetap lewat node/proxy sehat.
