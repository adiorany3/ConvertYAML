# Fresh Candidate Pool untuk OpenWrt ↔ GitHub

Tujuan fitur ini adalah mencegah kondisi semua node mati sebelum OpenWrt sempat mendapat akun baru.
GitHub akan selalu menyiapkan kandidat node yang sudah dites, lalu OpenWrt bisa mengambil config fresh saat AutoPilot mendeteksi banyak kegagalan.

## File yang dibuat GitHub

- `openclash_fresh_pool.yaml` — config cadangan berisi kandidat fresh yang sudah lolos URL test Mihomo.
- `fresh_pool/fresh_candidates.txt` — akun kandidat fresh hasil URL test.
- `fresh_pool/fresh_candidates_strict.txt` — akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json` — metadata kandidat.
- `fresh_pool/fresh_candidates_report.md` — laporan ringkas.

## Cara kerja

```text
GitHub Action generate node
↓
Mihomo URL test + NekoBox/sing-box test
↓
openclash_auto.yaml dibuat untuk harian
↓
openclash_fresh_pool.yaml dibuat sebagai cadangan fresh
↓
OpenWrt fresh_guard memantau log AutoPilot
↓
Jika banyak FAIL/timeout/503/504 → router pull openclash_fresh_pool.yaml
↓
OpenClash restart + force-after-reload + avoid-direct
```

## Install di OpenWrt

```sh
opkg update
opkg install python3 curl ca-certificates
cd /root/scripts
sh install_router_github_sync_openwrt.sh
```

Edit env:

```sh
vi /etc/mihomo-autopilot/github.env
```

Minimal:

```sh
GITHUB_REPO='username/repo'
GITHUB_BRANCH='main'
GITHUB_TOKEN='isi_token_github'
MIHOMO_API='http://127.0.0.1:9090'
MIHOMO_SECRET='reyre'
CONFIG_NAME='openclash_auto.yaml'
FRESH_CONFIG_NAME='openclash_fresh_pool.yaml'
FRESH_FAIL_THRESHOLD='6'
FRESH_PULL_COOLDOWN_SECONDS='900'
FRESH_TRIGGER_REBUILD='1'
```

## Pull fresh manual

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

## Guard otomatis

Installer menambahkan cron:

```sh
*/5 * * * * . /etc/mihomo-autopilot/github.env; sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh >> /tmp/mihomo_fresh_guard.log 2>&1
```

Cek log:

```sh
tail -f /tmp/mihomo_fresh_guard.log
```

## Download kandidat saja tanpa memasang config

```sh
. /etc/mihomo-autopilot/github.env
sh /etc/mihomo-autopilot/openwrt_download_fresh_candidates.sh
ls -lh /etc/mihomo-autopilot/fresh_pool
```

## Catatan

- Fresh pool akan mencoba `openclash_fresh_pool.yaml` dulu.
- Jika gagal, script fallback ke `openclash_auto.yaml`, lalu `openclash_lite.yaml`.
- Config lama tetap dibackup oleh `openwrt_pull_config.sh` dan bisa rollback otomatis.
- Fitur ini tidak melakukan scanning random; hanya memakai kandidat dari subscription/manual source yang sudah ada di repo.
