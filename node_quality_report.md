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
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-70MS
- AKUN-006-UNKNOWN-VLESS-WS-80MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-005-UNKNOWN-VLESS-WS-92MS
- AKUN-007-UNKNOWN-VLESS-WS-112MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-70MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-010-CLOUDFLARE-VLESS-WS-234MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-70MS
- AKUN-006-UNKNOWN-VLESS-WS-80MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-005-UNKNOWN-VLESS-WS-92MS
- AKUN-007-UNKNOWN-VLESS-WS-112MS
- AKUN-010-CLOUDFLARE-VLESS-WS-234MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-86MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-CLOUDFLARE-VLESS-WS-73MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-98MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-74MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-96MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-UNKNOWN-VLESS-WS-101MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
