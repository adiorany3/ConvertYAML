# Patch Notes - No DIRECT After OpenClash Reload

Tujuan patch ini adalah mencegah koneksi jatuh ke `DIRECT` setelah OpenClash reload/restart.

## Perubahan utama

- AutoPilot sekarang mendukung flag `--avoid-direct`.
- `force_after_openclash_reload.sh` default memakai `FORCE_AVOID_DIRECT=1`.
- Setelah reload, force-after-reload akan memilih jalur proxy sehat seperti `WARM-UP`, `WARM-UP-CF`, `AUTO-FAST`, `STREAMING-FAST`, atau `FALLBACK`, dan tidak memilih `DIRECT`.
- Jika selector sebelumnya berada di `DIRECT`, AutoPilot akan memindahkannya ke kandidat proxy sehat pertama.
- Semua selector YAML dibuat menaruh `DIRECT` di urutan paling akhir agar fresh import/reload tidak mudah jatuh ke direct.
- `CLEAN` juga diubah dari `DIRECT` paling depan menjadi `DIRECT` paling akhir.
- Installer OpenWrt menyimpan variabel `FORCE_AVOID_DIRECT='1'` ke `/etc/mihomo-autopilot/github.env`.

## Cara pakai di OpenWrt

Install ulang patch force-after-reload:

```sh
cd /root/scripts
MIHOMO_SECRET='reyre' FORCE_AVOID_DIRECT=1 sh install_force_after_reload_openwrt.sh
```

Tes manual:

```sh
FORCE_AVOID_DIRECT=1 sh /etc/mihomo-autopilot/force_after_openclash_reload.sh
```

Reload OpenClash sekaligus paksa proxy siap:

```sh
openclash-reload-autopilot restart
```

Cek log:

```sh
tail -f /tmp/mihomo_force_after_reload.log
```

## Catatan

`DIRECT` masih tetap ada sebagai opsi manual darurat, tetapi tidak dipilih oleh force-after-reload. Rule LAN/lokal tetap `DIRECT` agar akses router, perangkat lokal, dan jaringan internal tidak rusak.
