# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-ZOOM-VLESS-WS-67MS
- AKUN-001-UNKNOWN-VLESS-WS-69MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-SEECK-VLESS-WS-93MS
- AKUN-006-UNKNOWN-VLESS-WS-101MS
- AKUN-004-UNKNOWN-VLESS-WS-102MS
- AKUN-007-CLOUDFLARE-VLESS-WS-108MS

## Tier 1B - WARM-UP-CF
- AKUN-007-CLOUDFLARE-VLESS-WS-108MS

## Streaming Pool
- AKUN-002-ZOOM-VLESS-WS-67MS
- AKUN-001-UNKNOWN-VLESS-WS-69MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-008-UNKNOWN-VLESS-WS-91MS
- AKUN-005-SEECK-VLESS-WS-93MS
- AKUN-006-UNKNOWN-VLESS-WS-101MS
- AKUN-004-UNKNOWN-VLESS-WS-102MS
- AKUN-007-CLOUDFLARE-VLESS-WS-108MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-SPEEDTEST-VLESS-WS-78MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-DEV-VLESS-WS-92MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-99MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-DEV-VLESS-WS-104MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
