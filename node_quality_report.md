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
- AKUN-001-VULTR-VLESS-WS-65MS
- AKUN-003-CLOUDFLARE-VLESS-WS-72MS
- AKUN-002-CLOUDFLARE-VLESS-WS-74MS
- AKUN-005-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-007-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-103MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-72MS
- AKUN-002-CLOUDFLARE-VLESS-WS-74MS
- AKUN-005-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-103MS

## Streaming Pool
- AKUN-001-VULTR-VLESS-WS-65MS
- AKUN-003-CLOUDFLARE-VLESS-WS-72MS
- AKUN-002-CLOUDFLARE-VLESS-WS-74MS
- AKUN-005-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-007-CLOUDFLARE-VLESS-WS-87MS
- AKUN-008-UNKNOWN-VLESS-WS-94MS
- AKUN-006-CLOUDFLARE-VLESS-WS-103MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-CLOUDFLARE-VLESS-WS-91MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-106MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-011-UNKNOWN-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
