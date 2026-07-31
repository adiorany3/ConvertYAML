# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-ICOOK-VLESS-WS-224MS
- AKUN-006-UNKNOWN-VLESS-WS-236MS
- AKUN-001-UNKNOWN-VLESS-WS-236MS
- AKUN-004-CLOUDFLARE-VLESS-WS-236MS
- AKUN-005-UNKNOWN-VLESS-WS-238MS
- AKUN-003-CLOUDFLARE-VLESS-WS-242MS
- AKUN-007-RMGYVPN-VLESS-WS-537MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-236MS
- AKUN-003-CLOUDFLARE-VLESS-WS-242MS
- AKUN-009-CLOUDFLARE-VLESS-WS-348MS

## Streaming Pool
- AKUN-002-ICOOK-VLESS-WS-224MS
- AKUN-006-UNKNOWN-VLESS-WS-236MS
- AKUN-001-UNKNOWN-VLESS-WS-236MS
- AKUN-004-CLOUDFLARE-VLESS-WS-236MS
- AKUN-005-UNKNOWN-VLESS-WS-238MS
- AKUN-003-CLOUDFLARE-VLESS-WS-242MS
- AKUN-009-CLOUDFLARE-VLESS-WS-348MS
- AKUN-007-RMGYVPN-VLESS-WS-537MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
