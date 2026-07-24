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
- AKUN-001-CLOUDFLARE-VLESS-WS-77MS
- AKUN-002-ZVC-VLESS-WS-80MS
- AKUN-003-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-90MS
- AKUN-007-CLOUDFLARE-VLESS-WS-93MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-90MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-77MS
- AKUN-002-ZVC-VLESS-WS-80MS
- AKUN-003-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-90MS
- AKUN-007-CLOUDFLARE-VLESS-WS-93MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS
- AKUN-008-UNKNOWN-VLESS-WS-97MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-CLOUDFLARE-VLESS-WS-88MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
