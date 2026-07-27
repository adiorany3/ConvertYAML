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
- AKUN-001-CLOUDFLARE-VLESS-WS-60MS
- AKUN-002-UNKNOWN-VLESS-WS-60MS
- AKUN-005-CLOUDFLARE-VLESS-WS-60MS
- AKUN-003-DEV-VLESS-WS-61MS
- AKUN-004-CLOUDFLARE-VLESS-WS-70MS
- AKUN-006-ZVC-VLESS-WS-81MS
- AKUN-007-CLOUDFLARE-VLESS-WS-93MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-60MS
- AKUN-005-CLOUDFLARE-VLESS-WS-60MS
- AKUN-003-DEV-VLESS-WS-61MS
- AKUN-004-CLOUDFLARE-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-93MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-60MS
- AKUN-002-UNKNOWN-VLESS-WS-60MS
- AKUN-005-CLOUDFLARE-VLESS-WS-60MS
- AKUN-003-DEV-VLESS-WS-61MS
- AKUN-004-CLOUDFLARE-VLESS-WS-70MS
- AKUN-006-ZVC-VLESS-WS-81MS
- AKUN-007-CLOUDFLARE-VLESS-WS-93MS
- AKUN-008-CLOUDFLARE-VLESS-WS-102MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-SPEEDTEST-VLESS-WS-65MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
