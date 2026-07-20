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
- AKUN-006-ZVC-VLESS-WS-82MS
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-86MS
- AKUN-002-CLOUDFLARE-VLESS-WS-89MS
- AKUN-007-CLOUDFLARE-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-95MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-002-CLOUDFLARE-VLESS-WS-89MS
- AKUN-007-CLOUDFLARE-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-95MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS

## Streaming Pool
- AKUN-008-UNKNOWN-VLESS-WS-81MS
- AKUN-006-ZVC-VLESS-WS-82MS
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-86MS
- AKUN-002-CLOUDFLARE-VLESS-WS-89MS
- AKUN-007-CLOUDFLARE-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-95MS
- AKUN-004-CLOUDFLARE-VLESS-WS-96MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-88MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
