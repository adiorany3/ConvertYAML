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
- AKUN-003-CLOUDFLARE-VLESS-WS-88MS
- AKUN-001-CLOUDFLARE-VLESS-WS-89MS
- AKUN-004-CLOUDFLARE-VLESS-WS-90MS
- AKUN-002-UNKNOWN-VLESS-WS-91MS
- AKUN-006-WPENG-VLESS-WS-93MS
- AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-99MS
- AKUN-007-CLOUDFLARE-VLESS-WS-101MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-88MS
- AKUN-001-CLOUDFLARE-VLESS-WS-89MS
- AKUN-004-CLOUDFLARE-VLESS-WS-90MS
- AKUN-007-CLOUDFLARE-VLESS-WS-101MS
- AKUN-008-CLOUDFLARE-VLESS-WS-115MS

## Streaming Pool
- AKUN-003-CLOUDFLARE-VLESS-WS-88MS
- AKUN-001-CLOUDFLARE-VLESS-WS-89MS
- AKUN-004-CLOUDFLARE-VLESS-WS-90MS
- AKUN-002-UNKNOWN-VLESS-WS-91MS
- AKUN-006-WPENG-VLESS-WS-93MS
- AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-99MS
- AKUN-007-CLOUDFLARE-VLESS-WS-101MS
- AKUN-008-CLOUDFLARE-VLESS-WS-115MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
