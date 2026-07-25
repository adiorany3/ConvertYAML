# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-003-ZVC-VLESS-WS-77MS
- AKUN-002-UNKNOWN-VLESS-WS-77MS
- AKUN-001-UNKNOWN-VLESS-WS-78MS
- AKUN-004-UNKNOWN-VLESS-WS-85MS
- AKUN-005-3666888-VLESS-WS-95MS
- AKUN-007-UNKNOWN-VLESS-WS-100MS
- AKUN-006-UNKNOWN-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-126MS
- AKUN-010-CLOUDFLARE-VLESS-WS-179MS

## Streaming Pool
- AKUN-003-ZVC-VLESS-WS-77MS
- AKUN-002-UNKNOWN-VLESS-WS-77MS
- AKUN-001-UNKNOWN-VLESS-WS-78MS
- AKUN-004-UNKNOWN-VLESS-WS-85MS
- AKUN-005-3666888-VLESS-WS-95MS
- AKUN-006-UNKNOWN-VLESS-WS-107MS
- AKUN-009-CLOUDFLARE-VLESS-WS-126MS
- AKUN-010-CLOUDFLARE-VLESS-WS-179MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-SPEEDTEST-VLESS-WS-83MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-SPEEDTEST-VLESS-WS-99MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
