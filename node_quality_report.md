# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-88MS
- AKUN-006-MEDIUM-VLESS-WS-96MS
- AKUN-003-UNKNOWN-VLESS-WS-98MS
- AKUN-002-CLOUDFLARE-VLESS-WS-102MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-005-EU-VLESS-WS-112MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-102MS
- AKUN-010-DEV-VLESS-WS-103MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-88MS
- AKUN-006-MEDIUM-VLESS-WS-96MS
- AKUN-003-UNKNOWN-VLESS-WS-98MS
- AKUN-002-CLOUDFLARE-VLESS-WS-102MS
- AKUN-010-DEV-VLESS-WS-103MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-005-EU-VLESS-WS-112MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-CLOUDFLARE-VLESS-WS-102MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
