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
- AKUN-001-CLOUDFLARE-VLESS-WS-76MS
- AKUN-007-CLOUDFLARE-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-82MS
- AKUN-002-WPENG-VLESS-WS-83MS
- AKUN-003-ZVC-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-76MS
- AKUN-007-CLOUDFLARE-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-82MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-76MS
- AKUN-007-CLOUDFLARE-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-82MS
- AKUN-002-WPENG-VLESS-WS-83MS
- AKUN-003-ZVC-VLESS-WS-84MS
- AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
