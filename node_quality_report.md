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
- AKUN-003-WEBEX-VLESS-WS-90MS
- AKUN-001-CLOUDFLARE-VLESS-WS-92MS
- AKUN-002-CLOUDFLARE-VLESS-WS-94MS
- AKUN-004-ZVC-VLESS-WS-96MS
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS
- AKUN-005-UNKNOWN-VLESS-WS-104MS
- AKUN-007-MEDIUM-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-92MS
- AKUN-002-CLOUDFLARE-VLESS-WS-94MS
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS
- AKUN-008-CLOUDFLARE-VLESS-WS-100MS
- AKUN-009-CLOUDFLARE-VLESS-WS-138MS

## Streaming Pool
- AKUN-003-WEBEX-VLESS-WS-90MS
- AKUN-001-CLOUDFLARE-VLESS-WS-92MS
- AKUN-002-CLOUDFLARE-VLESS-WS-94MS
- AKUN-004-ZVC-VLESS-WS-96MS
- AKUN-006-CLOUDFLARE-VLESS-WS-98MS
- AKUN-008-CLOUDFLARE-VLESS-WS-100MS
- AKUN-005-UNKNOWN-VLESS-WS-104MS
- AKUN-009-CLOUDFLARE-VLESS-WS-138MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-UNKNOWN-VLESS-WS-114MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-129MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-DEV-VLESS-WS-160MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
