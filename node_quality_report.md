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
- AKUN-001-CLOUDFLARE-VLESS-WS-82MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-006-UNKNOWN-VLESS-WS-93MS
- AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-102MS
- AKUN-003-UNKNOWN-VLESS-WS-106MS
- AKUN-005-ZOOM-VLESS-WS-111MS
- AKUN-007-UNKNOWN-VLESS-WS-119MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-80MS
- AKUN-001-CLOUDFLARE-VLESS-WS-82MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-010-CLOUDFLARE-VLESS-WS-136MS

## Streaming Pool
- AKUN-009-CLOUDFLARE-VLESS-WS-80MS
- AKUN-001-CLOUDFLARE-VLESS-WS-82MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-006-UNKNOWN-VLESS-WS-93MS
- AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-102MS
- AKUN-003-UNKNOWN-VLESS-WS-106MS
- AKUN-005-ZOOM-VLESS-WS-111MS
- AKUN-010-CLOUDFLARE-VLESS-WS-136MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-100MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-120MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
