# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS
- AKUN-002-UNKNOWN-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-004-CLOUDFLARE-VLESS-WS-101MS
- AKUN-007-UNKNOWN-VLESS-WS-103MS
- AKUN-005-UNKNOWN-VLESS-WS-105MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-004-CLOUDFLARE-VLESS-WS-101MS
- AKUN-008-CLOUDFLARE-VLESS-WS-115MS
- AKUN-010-CLOUDFLARE-VLESS-WS-286MS

## Streaming Pool
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS
- AKUN-002-UNKNOWN-VLESS-WS-87MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-004-CLOUDFLARE-VLESS-WS-101MS
- AKUN-005-UNKNOWN-VLESS-WS-105MS
- AKUN-008-CLOUDFLARE-VLESS-WS-115MS
- AKUN-010-CLOUDFLARE-VLESS-WS-286MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-97MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
