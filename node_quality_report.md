# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-194MS
- AKUN-004-CLOUDFLARE-VLESS-WS-195MS
- AKUN-003-UNKNOWN-VLESS-WS-196MS
- AKUN-005-UNKNOWN-VLESS-WS-224MS
- AKUN-006-UNKNOWN-VLESS-WS-234MS
- AKUN-002-CLOUDFLARE-VLESS-WS-247MS
- AKUN-007-UNKNOWN-VLESS-WS-251MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-194MS
- AKUN-004-CLOUDFLARE-VLESS-WS-195MS
- AKUN-008-CLOUDFLARE-VLESS-WS-242MS
- AKUN-002-CLOUDFLARE-VLESS-WS-247MS
- AKUN-010-CLOUDFLARE-VLESS-WS-278MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-194MS
- AKUN-004-CLOUDFLARE-VLESS-WS-195MS
- AKUN-003-UNKNOWN-VLESS-WS-196MS
- AKUN-005-UNKNOWN-VLESS-WS-224MS
- AKUN-006-UNKNOWN-VLESS-WS-234MS
- AKUN-008-CLOUDFLARE-VLESS-WS-242MS
- AKUN-002-CLOUDFLARE-VLESS-WS-247MS
- AKUN-010-CLOUDFLARE-VLESS-WS-278MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
