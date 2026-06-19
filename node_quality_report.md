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
- AKUN-001-UNKNOWN-VLESS-WS-65MS
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-002-CLOUDFLARE-VLESS-WS-69MS
- AKUN-005-CLOUDFLARE-VLESS-WS-70MS
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-002-CLOUDFLARE-VLESS-WS-69MS
- AKUN-005-CLOUDFLARE-VLESS-WS-70MS
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-65MS
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-002-CLOUDFLARE-VLESS-WS-69MS
- AKUN-005-CLOUDFLARE-VLESS-WS-70MS
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS
- AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-DEV-VLESS-WS-67MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-71MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-CLOUDFLARE-VLESS-WS-76MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-69MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-83MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-SPEEDTEST-VLESS-WS-138MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
