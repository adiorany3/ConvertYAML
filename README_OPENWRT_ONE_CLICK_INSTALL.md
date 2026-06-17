# OpenWrt One-Click Install / Reinstall

File utama:

```sh
scripts/install_reinstall_all_openwrt.sh
```

Script ini dibuat untuk memasang ulang seluruh toolkit ConvertYAML di OpenWrt tanpa menghilangkan setting yang sudah berhasil.

## Prinsip Aman

- Tidak menimpa `/etc/mihomo-autopilot/github.env` kalau file sudah ada.
- Tidak menghapus token GitHub, secret Mihomo, nama repo, branch, dan setting lain di `github.env`.
- Membuat backup `github.env` ke `/etc/mihomo-autopilot/backups/` saat reinstall.
- Membuat backup crontab lama sebelum memasang ulang cron project.
- Menghapus duplikasi cron lama khusus project ConvertYAML, tetapi cron lain milik router tetap dipertahankan.
- Menyalin ulang semua script terbaru ke `/etc/mihomo-autopilot`.
- Memasang ulang wrapper `openclash-reload-autopilot`.
- Memeriksa dependency, file wajib, cron, wrapper, dan akses Mihomo API.

## Cara Pakai

Upload folder `scripts` dari ZIP ke router, misalnya ke:

```text
/root/scripts
```

Lalu jalankan:

```sh
cd /root/scripts
sh install_reinstall_all_openwrt.sh
```

Untuk hanya memeriksa tanpa mengubah apa pun:

```sh
sh /etc/mihomo-autopilot/install_reinstall_all_openwrt.sh check
```

Atau dari folder upload:

```sh
cd /root/scripts
sh install_reinstall_all_openwrt.sh check
```

## Dependency

Default script akan mencoba memasang dependency berikut kalau belum ada:

```sh
opkg update
opkg install python3 curl ca-certificates
```

Kalau tidak ingin script install package otomatis:

```sh
INSTALL_PACKAGES=0 sh install_reinstall_all_openwrt.sh
```

## File Env Tidak Ditimpa

Kalau file ini sudah ada:

```text
/etc/mihomo-autopilot/github.env
```

maka script hanya melakukan backup dan permission check. Isi file tidak diubah.

Kalau file belum ada, script membuat template baru dengan default:

```sh
MIHOMO_API='http://127.0.0.1:9090'
MIHOMO_SECRET='reyre'
```

## Cron yang Dipasang

Script memasang block cron managed:

- AutoPilot setiap 2 menit
- Force ping semua akun setiap 10 menit
- Router feedback ke GitHub setiap 15 menit
- Pull config GitHub setiap 3 jam
- Fresh guard setiap 5 menit
- Force after reload saat boot
- Reload guard setiap 1 menit

Cron lain di router tetap dipertahankan.

## Tes Setelah Install

```sh
sh /etc/mihomo-autopilot/install_reinstall_all_openwrt.sh check
```

```sh
openclash-reload-autopilot restart
```

```sh
tail -f /tmp/mihomo_autopilot.log
```

```sh
tail -f /tmp/mihomo_force_after_reload.log
```

```sh
tail -f /tmp/mihomo_fresh_guard.log
```

## Jika Mihomo API 401

Pastikan file env berisi secret yang benar:

```sh
vi /etc/mihomo-autopilot/github.env
```

Contoh:

```sh
MIHOMO_SECRET='reyre'
```

Lalu cek ulang:

```sh
sh /etc/mihomo-autopilot/install_reinstall_all_openwrt.sh check
```
