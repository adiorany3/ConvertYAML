# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-002-UNKNOWN-VLESS-WS-123MS
- AKUN-007-UNKNOWN-VLESS-WS-125MS
- AKUN-003-DEV-VLESS-WS-127MS
- AKUN-005-UNKNOWN-VLESS-WS-128MS
- AKUN-006-UNKNOWN-VLESS-WS-128MS
- AKUN-004-CLOUDFLARE-VLESS-WS-131MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-010-CLOUDFLARE-VLESS-WS-119MS
- AKUN-003-DEV-VLESS-WS-127MS
- AKUN-004-CLOUDFLARE-VLESS-WS-131MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-010-CLOUDFLARE-VLESS-WS-119MS
- AKUN-002-UNKNOWN-VLESS-WS-123MS
- AKUN-007-UNKNOWN-VLESS-WS-125MS
- AKUN-003-DEV-VLESS-WS-127MS
- AKUN-005-UNKNOWN-VLESS-WS-128MS
- AKUN-006-UNKNOWN-VLESS-WS-128MS
- AKUN-004-CLOUDFLARE-VLESS-WS-131MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-112MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-002-CLOUDFLARE-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-127MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-DEV-VLESS-WS-125MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-UNKNOWN-VLESS-WS-121MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-125MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-CLOUDFLARE-VLESS-WS-120MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-017-UNKNOWN-VLESS-WS-123MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-020-ZVC-VLESS-WS-141MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-021-CLOUDFLARE-VLESS-WS-128MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
