# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-ORACLE-VLESS-WS-67MS
- AKUN-002-CLOUDFLARE-VLESS-WS-75MS
- AKUN-005-BIGCOMMERCE-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-89MS
- AKUN-007-COMPREND-NET-VLESS-WS-90MS
- AKUN-006-COMPREND-NET-VLESS-WS-92MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-89MS

## Streaming Pool
- AKUN-001-ORACLE-VLESS-WS-67MS
- AKUN-002-CLOUDFLARE-VLESS-WS-75MS
- AKUN-005-BIGCOMMERCE-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-89MS
- AKUN-007-COMPREND-NET-VLESS-WS-90MS
- AKUN-008-UNKNOWN-VLESS-WS-90MS
- AKUN-006-COMPREND-NET-VLESS-WS-92MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-96MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-88MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-DEV-VLESS-WS-83MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
