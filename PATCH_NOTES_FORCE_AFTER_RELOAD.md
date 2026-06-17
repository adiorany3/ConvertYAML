# Patch Notes — Force After OpenClash Reload

Patch ini menambahkan mekanisme agar setelah OpenClash/Mihomo reload/restart, router tidak menunggu lama sampai node siap.

## File baru

- `scripts/force_after_openclash_reload.sh`
- `scripts/openclash_reload_guard.sh`
- `scripts/install_force_after_reload_openwrt.sh`

## Fungsi utama

1. Menunggu Mihomo API aktif setelah OpenClash reload.
2. Menjalankan AutoPilot beberapa kali secara cepat.
3. Memilih group/node sehat seperti `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, atau `STREAMING-FAST`.
4. Menutup koneksi lama agar traffic baru langsung memakai jalur yang sudah sehat.
5. Guard cron mendeteksi PID core Mihomo/Clash berubah setelah reload dari LuCI/OpenClash.

## Cara pakai cepat di OpenWrt

```sh
opkg update
opkg install python3 curl ca-certificates
cd /root/scripts
MIHOMO_SECRET='reyre' sh install_force_after_reload_openwrt.sh
```

Tes manual:

```sh
sh /etc/mihomo-autopilot/force_after_openclash_reload.sh
```

Reload OpenClash + paksa node siap:

```sh
openclash-reload-autopilot restart
```

Lihat log:

```sh
tail -f /tmp/mihomo_force_after_reload.log
```

## Env opsional

```sh
FORCE_WAIT_SECONDS='90'
FORCE_PASSES='3'
FORCE_SLEEP_BETWEEN='5'
FORCE_FLUSH_FAKEIP='0'
```

`FORCE_FLUSH_FAKEIP='1'` bisa dicoba kalau DNS/fake-ip sering nyangkut, tetapi default dibuat `0` agar aman.
