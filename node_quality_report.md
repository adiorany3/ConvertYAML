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
- AKUN-002-CLOUDFLARE-VLESS-WS-99MS
- AKUN-001-CLOUDFLARE-VLESS-WS-100MS
- AKUN-003-CLOUDFLARE-VLESS-WS-108MS
- AKUN-005-UNKNOWN-VLESS-WS-109MS
- AKUN-006-DEV-VLESS-WS-109MS
- AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-110MS
- AKUN-007-DEV-VLESS-WS-111MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-99MS
- AKUN-001-CLOUDFLARE-VLESS-WS-100MS
- AKUN-003-CLOUDFLARE-VLESS-WS-108MS
- AKUN-006-DEV-VLESS-WS-109MS
- AKUN-007-DEV-VLESS-WS-111MS

## Streaming Pool
- AKUN-008-466688-VLESS-WS-90MS
- AKUN-002-CLOUDFLARE-VLESS-WS-99MS
- AKUN-001-CLOUDFLARE-VLESS-WS-100MS
- AKUN-003-CLOUDFLARE-VLESS-WS-108MS
- AKUN-005-UNKNOWN-VLESS-WS-109MS
- AKUN-006-DEV-VLESS-WS-109MS
- AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-110MS
- AKUN-007-DEV-VLESS-WS-111MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-114MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
