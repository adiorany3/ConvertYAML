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
- AKUN-001-CLOUDFLARE-VLESS-WS-104MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-002-CLOUDFLARE-VLESS-WS-122MS
- AKUN-005-CLOUDFLARE-VLESS-WS-123MS
- AKUN-004-DEV-VLESS-WS-125MS
- AKUN-006-CLOUDFLARE-VLESS-WS-126MS
- AKUN-007-UNKNOWN-VLESS-WS-137MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-104MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-002-CLOUDFLARE-VLESS-WS-122MS
- AKUN-005-CLOUDFLARE-VLESS-WS-123MS
- AKUN-004-DEV-VLESS-WS-125MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-104MS
- AKUN-008-CLOUDFLARE-VLESS-WS-116MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-002-CLOUDFLARE-VLESS-WS-122MS
- AKUN-005-CLOUDFLARE-VLESS-WS-123MS
- AKUN-004-DEV-VLESS-WS-125MS
- AKUN-006-CLOUDFLARE-VLESS-WS-126MS
- AKUN-007-UNKNOWN-VLESS-WS-137MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-CLOUDFLARE-VLESS-WS-98MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-NODEJS-VLESS-WS-102MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
