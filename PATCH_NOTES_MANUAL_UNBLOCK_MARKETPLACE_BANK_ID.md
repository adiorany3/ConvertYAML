# Patch Notes - Manual Unblock Marketplace, Bank, dan Website Indonesia

Perubahan:
- `manual_unblock_domains.txt` diperluas dengan daftar marketplace/e-commerce, bank, fintech/payment gateway, ekspedisi, operator, media, edukasi/job platform, dan catch-all domain Indonesia.
- Menambahkan rule `DOMAIN-SUFFIX,id` agar mayoritas website Indonesia berbasis TLD `.id` otomatis masuk group `MANUAL`.
- Rule sudah disuntikkan ke YAML berbasis rules: `openclash_auto.yaml`, `openclash_lite.yaml`, dan `openclash_safe_names_rule_split.yaml`.
- Rule LAN/private tetap berada sebelum daftar manual agar akses router/perangkat lokal tetap aman `DIRECT`.

Catatan:
- Akses bank melalui proxy/manual node bisa memicu verifikasi keamanan tambahan atau pemblokiran sesi. Gunakan hanya jika memang diperlukan.
