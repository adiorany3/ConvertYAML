# Patch Notes — AutoPilot Self-Healing

Versi ini menambahkan sistem pemulihan otomatis untuk OpenClash/Mihomo agar koneksi lebih stabil, responsif, dan tidak terlalu lama menunggu node siap.

## Perubahan utama

1. Menambahkan folder `scripts/`:
   - `mihomo_autopilot.py`
   - `install_autopilot_openwrt.sh`
   - `run_autopilot_once.sh`

2. Menambahkan AutoPilot runtime:
   - Mengecek delay group utama via Mihomo External Controller.
   - Memilih jalur sehat secara otomatis.
   - Memberi cooldown pada group yang gagal berulang.
   - Menutup koneksi lama saat jalur berubah jika opsi `--close-connections` dipakai.

3. Policy selector:
   - `GLOBAL` dan `PROXY`: `WARM-UP → WARM-UP-CF → AUTO-FAST → FALLBACK → DIRECT`
   - `STREAMING`: `WARM-UP-CF → STREAMING-FAST → WARM-UP → AUTO-FAST → FALLBACK → DIRECT`
   - `SOCIAL-MEDIA`, `YOUTUBE`, `EDUKASI`: prioritas ke `WARM-UP` dan `WARM-UP-CF`.

4. Load-balance dibuat lebih stabil:
   - `LOAD-BALANCE` diubah ke `sticky-sessions` pada generator dan YAML utama.
   - Tujuannya agar koneksi panjang tidak terlalu sering berpindah jalur.

5. Workflow GitHub ditambah validasi:
   - Compile `scripts/mihomo_autopilot.py`
   - Syntax check shell installer
   - Commit file AutoPilot dan dokumentasi bila berubah

## Catatan penggunaan

AutoPilot membutuhkan External Controller OpenClash/Mihomo aktif di router. Default script memakai:

```text
http://127.0.0.1:9090
```

Jika config memakai secret, set:

```sh
MIHOMO_SECRET='isi_secret'
```

## Kenapa ini lebih smart?

YAML biasa hanya bisa health-check dan fallback. AutoPilot menambahkan logika runtime:

- gagal berulang → cooldown
- selector lambat → pindah jalur
- streaming diarahkan ke pool Cloudflare/streaming dulu
- koneksi lama yang nyangkut bisa ditutup otomatis

Ini membuat koneksi lebih self-healing tanpa harus klik manual di dashboard OpenClash.
