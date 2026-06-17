# Patch Responsif / Anti-Hibernasi Node

Patch ini dibuat untuk mengurangi kondisi node terasa delay atau seperti hibernasi saat OpenClash/Mihomo baru memakai node.

## Perubahan utama

1. `AUTO-FAST` dan `FALLBACK` health-check diturunkan dari 60 detik menjadi 30 detik.
2. `LOAD-BALANCE` diturunkan dari 120 detik menjadi 60 detik.
3. `lazy: false` dipertahankan agar health-check tetap aktif walau group belum dipilih.
4. TCP keep-alive global ditambahkan:
   - `keep-alive-interval: 15`
   - `keep-alive-idle: 600`
   - `disable-keep-alive: false`
5. `find-process-mode` untuk OpenClash router diubah ke `off` agar lebih ringan di router.
6. Manual node tidak hanya berada di group `MANUAL`; sekarang node manual juga dimasukkan langsung ke awal `FALLBACK` agar ikut di-health-check satu per satu.
7. Workflow GitHub Action diubah menjadi setiap 3 jam agar output node lebih sering refresh.
8. Default generator dan Streamlit app diselaraskan ke mode responsif.

## File yang diperbarui

- `sumberyaml_core.py`
- `generate_yaml.py`
- `streamlit_app.py`
- `.github/workflows/update-yaml-6jam.yml`
- `update-yaml-6jam.yml`
- `openclash_auto.yaml`
- `openclash_android.yaml`
- `README.md`
- `last_update.txt`
- `compatibility_report.txt`

## Catatan pemakaian

Untuk router OpenClash, gunakan `openclash_auto.yaml`.
Untuk Android/NekoBox-style config, gunakan `openclash_android.yaml`.

Jika router terasa berat, ubah `WAKEUP_INTERVAL` dari `30` ke `45` atau `60` di workflow.
