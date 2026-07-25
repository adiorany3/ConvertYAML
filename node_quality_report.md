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
- AKUN-002-CLOUDFLARE-VLESS-WS-57MS
- AKUN-005-ZVC-VLESS-WS-59MS
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-003-UNKNOWN-VLESS-WS-62MS
- AKUN-004-DEV-VLESS-WS-62MS
- AKUN-007-1PASSWORD-VLESS-WS-66MS
- AKUN-006-DEV-VLESS-WS-67MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-57MS
- AKUN-004-DEV-VLESS-WS-62MS
- AKUN-009-CLOUDFLARE-VLESS-WS-64MS
- AKUN-010-CLOUDFLARE-VLESS-WS-65MS
- AKUN-006-DEV-VLESS-WS-67MS

## Streaming Pool
- AKUN-002-CLOUDFLARE-VLESS-WS-57MS
- AKUN-005-ZVC-VLESS-WS-59MS
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-003-UNKNOWN-VLESS-WS-62MS
- AKUN-004-DEV-VLESS-WS-62MS
- AKUN-009-CLOUDFLARE-VLESS-WS-64MS
- AKUN-010-CLOUDFLARE-VLESS-WS-65MS
- AKUN-006-DEV-VLESS-WS-67MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-010-CLOUDFLARE-VLESS-WS-64MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
