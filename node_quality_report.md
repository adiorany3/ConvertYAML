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
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-005-CLOUDFLARE-VLESS-WS-91MS
- AKUN-007-466688-VLESS-WS-94MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-91MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-005-CLOUDFLARE-VLESS-WS-91MS
- AKUN-007-466688-VLESS-WS-94MS
- AKUN-008-CLOUDFLARE-VLESS-WS-101MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-81MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-86MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-DEV-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-CLOUDFLARE-VLESS-WS-95MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
