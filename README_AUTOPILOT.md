# AutoPilot Self-Healing untuk OpenClash/Mihomo

AutoPilot ini dibuat untuk membuat koneksi lebih stabil dan otomatis. Ia tidak mengganti config utama, tetapi memantau Mihomo/OpenClash lewat External Controller lalu memilih jalur terbaik secara berkala.

## Versi secret `reyre`

Paket ZIP ini sudah disesuaikan dengan secret OpenClash kamu:

```yaml
secret: "reyre"
```

File YAML yang sudah diberi secret:

- `openclash_auto.yaml`
- `openclash_lite.yaml`
- `openclash_safe_names_rule_split.yaml`

AutoPilot juga sudah default memakai `MIHOMO_SECRET='reyre'`. Kalau suatu saat secret di OpenClash kamu diganti, jalankan installer dengan env baru:

```sh
MIHOMO_SECRET='secret_baru' sh scripts/install_autopilot_openwrt.sh
```

## Fungsi utama

- Mengecek group utama: `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, `STREAMING-FAST`, dan `FALLBACK`.
- Memilih group sehat untuk selector `GLOBAL`, `PROXY`, `STREAMING`, `SOCIAL-MEDIA`, `YOUTUBE`, dan `EDUKASI`.
- Memberi cooldown sementara pada group yang gagal berulang agar tidak dipilih bolak-balik.
- Menampilkan pesan fix yang jelas kalau API terkena `401 Unauthorized`.
- Auto-detect secret dari env atau file config OpenClash jika memungkinkan.
- Opsional menutup koneksi lama ketika selector berpindah agar koneksi yang macet cepat pulih.
- Tetap aman untuk router karena default jalan tiap 2 menit, bukan spam tiap beberapa detik.

## Syarat OpenClash

Pastikan konfigurasi OpenClash memakai external controller, misalnya:

```yaml
external-controller: 0.0.0.0:9090
secret: "reyre"
```

Atau lebih aman kalau hanya dipakai dari router:

```yaml
external-controller: 127.0.0.1:9090
secret: "reyre"
```

Setelah upload YAML, restart OpenClash dulu.

## Tes manual di router

Upload folder `scripts` ke router, lalu jalankan:

```sh
MIHOMO_SECRET='reyre' python3 scripts/mihomo_autopilot.py --once --close-connections
```

Atau gunakan helper:

```sh
sh scripts/run_autopilot_once.sh
```

Kalau controller bukan port 9090:

```sh
MIHOMO_API='http://127.0.0.1:9090' MIHOMO_SECRET='reyre' python3 scripts/mihomo_autopilot.py --once --close-connections
```

## Install otomatis via cron OpenWrt

Dari folder repo/ZIP:

```sh
sh scripts/install_autopilot_openwrt.sh
```

Installer akan:

- Menyalin script ke `/etc/mihomo-autopilot/mihomo_autopilot.py`
- Menambahkan cron setiap 2 menit
- Memasang `MIHOMO_SECRET='reyre'` ke cron otomatis
- Menyimpan log ke `/tmp/mihomo_autopilot.log`

Cek cron:

```sh
crontab -l | grep mihomo_autopilot
```

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

## Troubleshooting 401 Unauthorized

Kalau muncul:

```text
HTTP Error 401: Unauthorized
```

jalankan:

```sh
MIHOMO_SECRET='reyre' python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

Lalu cek YAML OpenClash sudah punya:

```yaml
secret: "reyre"
```

Setelah itu restart:

```sh
/etc/init.d/openclash restart
/etc/init.d/cron restart
```

## File penting

- `scripts/mihomo_autopilot.py` — script utama AutoPilot.
- `scripts/install_autopilot_openwrt.sh` — installer cron OpenWrt.
- `scripts/run_autopilot_once.sh` — helper tes sekali jalan.
- `PATCH_NOTES_AUTOPILOT_SECRET_REYRE.md` — catatan perubahan secret fix.
