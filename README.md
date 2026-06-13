# SumberYAML OpenClash Bug-Compat Auto-Fast

Versi sederhana untuk Streamlit Online tanpa GitHub Action.

## Tujuan

Aplikasi ini mengambil akun publik dari link subscription bawaan, menyaring hanya port `443`, lalu membuat YAML OpenClash/Mihomo dengan `server` dipaksa ke bug server:

```text
104.17.3.81
```

## Perbaikan dari versi sebelumnya

Versi sebelumnya bisa menghasilkan sedikit akun hidup karena filter `120 ms` terlalu keras dan pengecekan belum sesuai dengan kondisi output server yang sudah diganti ke bug IP.

Versi ini memakai mode **bug compatibility check**:

1. Ambil node `vless://`, `vmess://`, `trojan://`, dan `ss://`.
2. Hanya node port `443` yang diproses.
3. Server output diganti ke `104.17.3.81`.
4. SNI/Host asli akun tetap dipertahankan.
5. Aplikasi mengetes TLS ke `104.17.3.81:443` memakai SNI/Host akun.
6. Node super cepat `≤120/123 ms` diprioritaskan.
7. Jika jumlah node super cepat kurang dari 20, aplikasi mengisi cadangan dari node yang tetap hidup/kompatibel bug server.
8. YAML memakai grup `GLOBAL` yang langsung mengarah ke `⚡ AUTO-FAST`.

## Output

- `openclash_bug_compat_auto_fast.yaml`
- `openclash_bug_compat_report.csv`

## Jalankan lokal

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy ke Streamlit Cloud

1. Upload semua file ke repository GitHub.
2. Buka Streamlit Cloud.
3. Pilih repository tersebut.
4. Main file: `streamlit_app.py`.
5. Deploy.

Tidak perlu GitHub Token dan tidak perlu GitHub Action.

## Catatan penting

Pengecekan aplikasi ini memastikan bug server `104.17.3.81` bisa melakukan TLS handshake dengan SNI/Host akun. Ini lebih sesuai untuk YAML yang server-nya dipaksa ke bug IP. Namun validasi proxy penuh tetap dilakukan oleh OpenClash melalui Health Check / Test Delay karena protokol VLESS/VMess/Trojan membutuhkan handshake lengkap di sisi client.
