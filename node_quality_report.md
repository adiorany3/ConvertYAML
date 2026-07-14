# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-002-UNKNOWN-VLESS-WS-64MS
- AKUN-004-CLOUDFLARE-VLESS-WS-64MS
- AKUN-003-466688-VLESS-WS-67MS
- AKUN-005-CLOUDFLARE-VLESS-WS-72MS
- AKUN-007-UNKNOWN-VLESS-WS-74MS
- AKUN-006-IDC-SG-VLESS-WS-89MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-64MS
- AKUN-009-CLOUDFLARE-VLESS-WS-70MS
- AKUN-008-CLOUDFLARE-VLESS-WS-70MS
- AKUN-005-CLOUDFLARE-VLESS-WS-72MS
- AKUN-010-CLOUDFLARE-VLESS-WS-119MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-002-UNKNOWN-VLESS-WS-64MS
- AKUN-004-CLOUDFLARE-VLESS-WS-64MS
- AKUN-003-466688-VLESS-WS-67MS
- AKUN-009-CLOUDFLARE-VLESS-WS-70MS
- AKUN-008-CLOUDFLARE-VLESS-WS-70MS
- AKUN-005-CLOUDFLARE-VLESS-WS-72MS
- AKUN-010-CLOUDFLARE-VLESS-WS-119MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-UNKNOWN-VLESS-WS-79MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
