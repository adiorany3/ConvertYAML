# Patch Notes - Smart Stable v2

Tanggal: 2026-06-17

## Tujuan
Membuat konfigurasi lebih stabil dan responsif tanpa membuat router terlalu berat akibat health-check berlebihan.

## Perubahan utama

1. **Smart Warm-Up Tiering**
   - `WARM-UP` tetap menjadi pool utama harian.
   - Pool dibuat kecil agar node utama selalu siap, bukan semua node dipaksa refresh cepat.

2. **Cloudflare Warm-Up khusus**
   - Menambah `WARM-UP-CF`.
   - Endpoint health-check: `https://cp.cloudflare.com`.
   - Ditujukan untuk node Cloudflare/Worker/VLESS WS agar lebih cepat bangun.

3. **Streaming-FAST lebih smart**
   - `STREAMING-FAST` memakai endpoint Cloudflare.
   - Isinya diprioritaskan dari node Cloudflare/WS + warm-up pool.
   - Tidak lagi hanya menduplikasi `WARM-UP` secara mentah.

4. **AUTO-FAST jadi Tier-2**
   - `AUTO-FAST` memakai fast pool, bukan dipaksa sebagai tempat semua cadangan.
   - Cadangan tetap disimpan di `FALLBACK`.

5. **FALLBACK lebih aman**
   - Urutan `FALLBACK`: automatic strict nodes dulu, manual nodes belakangan.
   - Manual node tetap ikut health-check langsung, tetapi tidak memperlambat pilihan pertama.

6. **Fake-IP filter diperluas**
   - Menambah filter untuk LAN, NTP, connectivity check, router gateway, dan domain perbankan Indonesia.

7. **Output Lite untuk router ringan**
   - Menambah `openclash_lite.yaml`.
   - Health-check lebih santai dan group lebih sedikit.

8. **Laporan kualitas node**
   - Menambah `node_quality_report.md`.
   - Berisi rekomendasi pemakaian, tier node, dan node yang gagal dari laporan NekoBox/sing-box terakhir.

## File yang terdampak
- `openclash_auto.yaml`
- `openclash_android.yaml`
- `openclash_lite.yaml`
- `node_quality_report.md`
- `generate_yaml.py`
- `sumberyaml_core.py`
- `streamlit_app.py`
- `.github/workflows/update-yaml-6jam.yml`
- `update-yaml-6jam.yml`

## Rekomendasi pemakaian
- OpenClash router normal: `openclash_auto.yaml`
- Router kecil/RAM terbatas: `openclash_lite.yaml`
- Android/NekoBox-like client: `openclash_android.yaml`
