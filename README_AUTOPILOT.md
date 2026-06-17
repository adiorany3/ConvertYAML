# AutoPilot Self-Healing untuk OpenClash/Mihomo

AutoPilot ini dibuat untuk membuat koneksi lebih stabil dan otomatis. Ia tidak mengganti config utama, tetapi memantau Mihomo/OpenClash lewat External Controller lalu memilih jalur terbaik secara berkala.

## Fungsi utama

- Mengecek group utama: `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, `STREAMING-FAST`, dan `FALLBACK`.
- Memilih group sehat untuk selector `GLOBAL`, `PROXY`, `STREAMING`, `SOCIAL-MEDIA`, `YOUTUBE`, dan `EDUKASI`.
- Memberi cooldown sementara pada group yang gagal berulang agar tidak dipilih bolak-balik.
- Opsional menutup koneksi lama ketika selector berpindah agar koneksi yang macet cepat pulih.
- Tetap aman untuk router karena default jalan tiap 2 menit, bukan spam tiap beberapa detik.

## Syarat OpenClash

Pastikan konfigurasi OpenClash memakai external controller, misalnya:

```yaml
external-controller: 0.0.0.0:9090
```

Atau lebih aman kalau hanya dipakai dari router:

```yaml
external-controller: 127.0.0.1:9090
```

Jika kamu memakai `secret`, jalankan AutoPilot dengan environment `MIHOMO_SECRET`.

## Tes manual di router

Upload folder `scripts` ke router, lalu jalankan:

```sh
python3 scripts/mihomo_autopilot.py --once --close-connections
```

Kalau OpenClash memakai secret:

```sh
MIHOMO_SECRET='isi_secret_kamu' python3 scripts/mihomo_autopilot.py --once --close-connections
```

Kalau controller bukan port 9090:

```sh
MIHOMO_API='http://127.0.0.1:9090' python3 scripts/mihomo_autopilot.py --once --close-connections
```

## Install otomatis via cron OpenWrt

Dari folder repo/ZIP:

```sh
sh scripts/install_autopilot_openwrt.sh
```

Installer akan:

- Menyalin script ke `/etc/mihomo-autopilot/mihomo_autopilot.py`
- Menambahkan cron setiap 2 menit
- Menyimpan log ke `/tmp/mihomo_autopilot.log`

Cek log:

```sh
tail -f /tmp/mihomo_autopilot.log
```

## Cara kerja pemilihan jalur

Untuk `GLOBAL` dan `PROXY`:

```text
WARM-UP → WARM-UP-CF → AUTO-FAST → FALLBACK → DIRECT
```

Untuk `STREAMING`:

```text
WARM-UP-CF → STREAMING-FAST → WARM-UP → AUTO-FAST → FALLBACK → DIRECT
```

Jika group gagal dua kali, group tersebut masuk cooldown 15 menit. Ini mencegah OpenClash bolak-balik memilih jalur yang sedang jelek.

## Rekomendasi setting aman

Default sudah aman:

```sh
python3 mihomo_autopilot.py --once --close-connections
```

Untuk koneksi yang sering macet parah, boleh tambah fake-ip flush:

```sh
python3 mihomo_autopilot.py --once --close-connections --flush-fakeip
```

Gunakan `--flush-fakeip` hanya jika perlu, karena beberapa core tidak mendukung endpoint flush yang sama.

## File penting

- `scripts/mihomo_autopilot.py` — script utama AutoPilot.
- `scripts/install_autopilot_openwrt.sh` — installer cron OpenWrt.
- `scripts/run_autopilot_once.sh` — helper tes sekali jalan.
- `PATCH_NOTES_AUTOPILOT_SELF_HEALING.md` — catatan perubahan versi ini.
