# Patch Notes - OpenWrt One-Click Install/Reinstall

## Ditambahkan

- `scripts/install_reinstall_all_openwrt.sh`
- `README_OPENWRT_ONE_CLICK_INSTALL.md`

## Fungsi

Script ini memasang ulang seluruh toolkit OpenWrt ConvertYAML secara aman dan idempotent.

Yang dilakukan:

- Check/install dependency `python3`, `curl`, `ca-certificates`.
- Menyalin ulang semua script utama ke `/etc/mihomo-autopilot`.
- Tidak menimpa `github.env` jika sudah ada.
- Membuat backup `github.env` dan crontab lama.
- Memasang ulang cron managed block.
- Memasang ulang wrapper `openclash-reload-autopilot`.
- Memeriksa file wajib, cron, wrapper, dan Mihomo API.

## Keamanan Env

`/etc/mihomo-autopilot/github.env` tidak diubah atau dihapus saat reinstall.
Jika belum ada, script baru membuat template default.
