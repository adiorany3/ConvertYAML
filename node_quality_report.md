# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-003-UBI-VLESS-WS-80MS
- AKUN-001-UNKNOWN-VLESS-WS-80MS
- AKUN-002-VULTR-VLESS-WS-83MS
- AKUN-005-466688-VLESS-WS-87MS
- AKUN-004-466688-VLESS-WS-92MS
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS
- AKUN-007-ZVC-VLESS-WS-101MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS

## Streaming Pool
- AKUN-003-UBI-VLESS-WS-80MS
- AKUN-001-UNKNOWN-VLESS-WS-80MS
- AKUN-002-VULTR-VLESS-WS-83MS
- AKUN-005-466688-VLESS-WS-87MS
- AKUN-004-466688-VLESS-WS-92MS
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS
- AKUN-007-ZVC-VLESS-WS-101MS
- AKUN-008-466688-VLESS-WS-111MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-006-DEV-VLESS-WS-95MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-UNKNOWN-VLESS-WS-102MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-010-CLOUDFLARE-VLESS-WS-104MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-DEV-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
