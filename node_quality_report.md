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
- AKUN-002-ZOOM-VLESS-WS-72MS
- AKUN-004-UNKNOWN-VLESS-WS-73MS
- AKUN-001-ZVC-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-77MS
- AKUN-007-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-101MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-77MS
- AKUN-007-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-86MS
- AKUN-008-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-101MS

## Streaming Pool
- AKUN-002-ZOOM-VLESS-WS-72MS
- AKUN-004-UNKNOWN-VLESS-WS-73MS
- AKUN-001-ZVC-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-77MS
- AKUN-007-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-86MS
- AKUN-008-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-101MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-UNKNOWN-VLESS-WS-68MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-82MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-010-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-128MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
