# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-58MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-003-WPENG-VLESS-WS-65MS
- AKUN-006-UNKNOWN-VLESS-WS-69MS
- AKUN-004-UNKNOWN-VLESS-WS-72MS
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-007-UNKNOWN-VLESS-WS-81MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-008-CLOUDFLARE-VLESS-WS-71MS
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-010-CLOUDFLARE-VLESS-WS-98MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-58MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-003-WPENG-VLESS-WS-65MS
- AKUN-006-UNKNOWN-VLESS-WS-69MS
- AKUN-008-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-UNKNOWN-VLESS-WS-72MS
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-010-CLOUDFLARE-VLESS-WS-98MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-68MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
