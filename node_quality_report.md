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
- AKUN-001-UNKNOWN-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-93MS
- AKUN-007-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-ZENFO-1-VLESS-WS-106MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-93MS
- AKUN-007-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-CLOUDFLARE-VLESS-WS-78MS
- AKUN-008-CLOUDFLARE-VLESS-WS-80MS
- AKUN-004-CLOUDFLARE-VLESS-WS-93MS
- AKUN-007-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-ZENFO-1-VLESS-WS-106MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-SPEEDTEST-VLESS-WS-72MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-79MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-SPEEDTEST-VLESS-WS-111MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-76MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
