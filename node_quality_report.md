# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-74MS
- AKUN-002-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-93MS
- AKUN-007-ZENFO-1-VLESS-WS-93MS
- AKUN-003-UNKNOWN-VLESS-WS-98MS
- AKUN-004-CLOUDFLARE-VLESS-WS-102MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-93MS
- AKUN-009-CLOUDFLARE-VLESS-WS-101MS
- AKUN-004-CLOUDFLARE-VLESS-WS-102MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-74MS
- AKUN-002-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-86MS
- AKUN-005-CLOUDFLARE-VLESS-WS-93MS
- AKUN-007-ZENFO-1-VLESS-WS-93MS
- AKUN-003-UNKNOWN-VLESS-WS-98MS
- AKUN-009-CLOUDFLARE-VLESS-WS-101MS
- AKUN-004-CLOUDFLARE-VLESS-WS-102MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-100MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-109MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
