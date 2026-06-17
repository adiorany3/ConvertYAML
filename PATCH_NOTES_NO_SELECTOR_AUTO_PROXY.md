# Patch Notes - No Selector Auto Proxy

Perubahan utama:

- Semua proxy-group `type: select` diubah menjadi otomatis `fallback`.
- `DIRECT` dihapus dari semua daftar `proxies` pada proxy-groups.
- `DIRECT` tetap dipertahankan hanya pada rules LAN/private agar akses lokal aman.
- `GLOBAL`, `PROXY`, `STREAMING`, `SOCIAL-MEDIA`, `YOUTUBE`, `EDUKASI`, `CLEAN`, dan `MANUAL` tidak lagi menjadi selector manual.
- `MANUAL` tetap menjadi target untuk domain di `manual_unblock_domains.txt`, tetapi sekarang otomatis dan tanpa `DIRECT`.
- AutoPilot policy ikut dibersihkan agar tidak mencoba memilih `DIRECT`.

Tujuan patch: setelah OpenClash reload/restart, koneksi otomatis memakai node sehat dan tidak jatuh ke DIRECT.
