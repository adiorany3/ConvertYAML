# Patch: PING-CHECK Force Delay

Masalah: akun/node yang sudah didapat kadang tampil abu-abu/no-ping di OpenClash setelah import/reload.

Perbaikan:
- Menambahkan group `PING-CHECK` bertipe `url-test` dengan `lazy: false` untuk memaksa semua akun dites delay oleh Mihomo/OpenClash.
- Menambahkan `scripts/mihomo_force_ping_all.py` untuk memanggil API `/proxies/<node>/delay` ke semua node.
- `force_after_openclash_reload.sh` sekarang menjalankan delay-check setelah OpenClash reload.
- Installer force-after-reload ikut menyalin script delay-check.

Catatan: kalau node tetap no-ping setelah patch ini, biasanya node memang tidak kompatibel dengan core/OpenClash, server bug sedang mati, atau secret/API belum cocok.
