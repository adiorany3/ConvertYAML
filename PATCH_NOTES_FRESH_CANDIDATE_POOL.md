# Patch Notes - Fresh Candidate Pool

## Tujuan

Mencegah kondisi OpenWrt kehabisan node sehat. GitHub sekarang selalu menyiapkan pool kandidat node fresh yang sudah diuji agar router bisa mengambil cadangan sebelum koneksi mati total.

## Perubahan

- Tambah output `openclash_fresh_pool.yaml`.
- Tambah folder `fresh_pool/`:
  - `fresh_candidates.txt`
  - `fresh_candidates_strict.txt`
  - `fresh_candidates.json`
  - `fresh_candidates_report.md`
- Tambah script OpenWrt:
  - `openwrt_pull_fresh_pool.sh`
  - `openwrt_fresh_guard.sh`
  - `openwrt_download_fresh_candidates.sh`
- Patch installer agar fresh guard berjalan otomatis setiap 5 menit.
- Patch workflow agar fresh pool ikut dibuat, divalidasi, dan dicommit.

## Mode aman

Fresh guard hanya aktif ketika log AutoPilot menunjukkan banyak `FAIL`, `timeout`, `503`, atau `504` dalam window terakhir. Ada cooldown agar router tidak pull/restart terus-menerus.
