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
- AKUN-005-CLOUDFLARE-VLESS-WS-69MS
- AKUN-003-CLOUDFLARE-VLESS-WS-70MS
- AKUN-001-CLOUDFLARE-VLESS-WS-71MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-004-SHOPIFY-VLESS-WS-75MS
- AKUN-002-UNKNOWN-VLESS-WS-78MS
- AKUN-006-UNKNOWN-VLESS-WS-85MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-69MS
- AKUN-003-CLOUDFLARE-VLESS-WS-70MS
- AKUN-001-CLOUDFLARE-VLESS-WS-71MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-009-CLOUDFLARE-VLESS-WS-82MS

## Streaming Pool
- AKUN-005-CLOUDFLARE-VLESS-WS-69MS
- AKUN-003-CLOUDFLARE-VLESS-WS-70MS
- AKUN-001-CLOUDFLARE-VLESS-WS-71MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-004-SHOPIFY-VLESS-WS-75MS
- AKUN-002-UNKNOWN-VLESS-WS-78MS
- AKUN-009-CLOUDFLARE-VLESS-WS-82MS
- AKUN-006-UNKNOWN-VLESS-WS-85MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-72MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
