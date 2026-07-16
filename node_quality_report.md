# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-IPXO-VLESS-WS-86MS
- AKUN-004-466688-VLESS-WS-90MS
- AKUN-002-466688-VLESS-WS-96MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-UNKNOWN-VLESS-WS-96MS
- AKUN-006-UNKNOWN-VLESS-WS-100MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS

## Streaming Pool
- AKUN-001-IPXO-VLESS-WS-86MS
- AKUN-004-466688-VLESS-WS-90MS
- AKUN-002-466688-VLESS-WS-96MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-UNKNOWN-VLESS-WS-96MS
- AKUN-006-UNKNOWN-VLESS-WS-100MS
- AKUN-008-UNKNOWN-VLESS-WS-102MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-DEV-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-UNKNOWN-VLESS-WS-101MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-009-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
