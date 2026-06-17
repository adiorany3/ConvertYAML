# Router ↔ GitHub Sync untuk OpenWrt + OpenClash

Versi ini membuat OpenWrt dan GitHub saling mengisi:

- **GitHub → OpenWrt**: router download config terbaru, backup config lama, validasi, restart OpenClash, lalu rollback otomatis kalau gagal.
- **OpenWrt → GitHub**: router membaca status Mihomo/OpenClash dan mengirim `router_feedback/*.json` ke repository.
- **Router trigger rebuild**: router bisa memicu GitHub Actions dengan `repository_dispatch` saat koneksi mulai buruk.
- **AutoPilot tetap aktif**: script self-healing tetap memilih `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, `STREAMING-FAST`, atau `FALLBACK`.

## File baru

```text
scripts/openwrt_pull_config.sh
scripts/openwrt_report_status.py
scripts/trigger_github_rebuild.sh
scripts/rollback_openclash_config.sh
scripts/install_router_github_sync_openwrt.sh
openwrt_github.env.example
.github/workflows/router-feedback.yml
router_feedback/.gitkeep
```

## 1. Upload ke router

Upload folder `scripts` ke router, misalnya ke:

```sh
/root/scripts
```

Lalu SSH ke OpenWrt:

```sh
opkg update
opkg install python3 curl ca-certificates
sh /root/scripts/install_router_github_sync_openwrt.sh
```

## 2. Isi konfigurasi GitHub di router

Edit:

```sh
vi /etc/mihomo-autopilot/github.env
```

Isi minimal:

```sh
GITHUB_REPO='username/repo'
GITHUB_BRANCH='main'
GITHUB_TOKEN='isi_token_github_kamu'
ROUTER_NAME='openwrt-home'

MIHOMO_API='http://127.0.0.1:9090'
MIHOMO_SECRET='reyre'
OPENCLASH_CONFIG_DIR='/etc/openclash/config'
CONFIG_NAME='openclash_auto.yaml'
```

Lalu amankan file:

```sh
chmod 600 /etc/mihomo-autopilot/github.env
```

## 3. Test manual

Test AutoPilot:

```sh
. /etc/mihomo-autopilot/github.env
python3 /etc/mihomo-autopilot/mihomo_autopilot.py --once --close-connections
```

Test laporan router ke GitHub:

```sh
. /etc/mihomo-autopilot/github.env
python3 /etc/mihomo-autopilot/openwrt_report_status.py --upload
```

Test pull config dari GitHub:

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/openwrt_pull_config.sh
```

Test trigger rebuild GitHub:

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/trigger_github_rebuild.sh "manual-test"
```

## 4. Cron otomatis

Installer memasang cron berikut:

```text
*/2 * * * * AutoPilot self-healing
*/15 * * * * Kirim feedback router ke GitHub
5 */3 * * * Pull config terbaru dari GitHub ke OpenWrt
```

Cek:

```sh
crontab -l
```

Log:

```sh
tail -f /tmp/mihomo_autopilot.log
tail -f /tmp/router_github_sync.log
```

## 5. Rollback manual

Kalau config baru bermasalah:

```sh
sh /etc/mihomo-autopilot/rollback_openclash_config.sh
```

## 6. Token GitHub yang dibutuhkan

Untuk repo private atau upload feedback, token perlu akses:

- Contents: read/write
- Actions/workflows: write jika ingin trigger workflow rebuild

Jangan simpan token di YAML OpenClash. Simpan hanya di:

```text
/etc/mihomo-autopilot/github.env
```

## 7. Catatan keamanan

- `MIHOMO_SECRET='reyre'` sudah sesuai config kamu.
- Kalau `external-controller` memakai `0.0.0.0:9090`, jangan kosongkan secret.
- Lebih aman gunakan `external-controller: 127.0.0.1:9090` jika API hanya dipakai dari router.
