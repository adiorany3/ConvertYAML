# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 7 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-77MS
- AKUN-002-UNKNOWN-VLESS-WS-82MS
- AKUN-007-ZOOM-VLESS-WS-82MS
- AKUN-004-UNKNOWN-VLESS-WS-85MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-UNKNOWN-VLESS-WS-88MS
- AKUN-006-MEDIUM-VLESS-WS-91MS

## Tier 1B - WARM-UP-CF
- AKUN-001-UNKNOWN-VLESS-WS-77MS
- AKUN-002-UNKNOWN-VLESS-WS-82MS
- AKUN-007-ZOOM-VLESS-WS-82MS
- AKUN-004-UNKNOWN-VLESS-WS-85MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-UNKNOWN-VLESS-WS-88MS
- AKUN-006-MEDIUM-VLESS-WS-91MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-77MS
- AKUN-002-UNKNOWN-VLESS-WS-82MS
- AKUN-007-ZOOM-VLESS-WS-82MS
- AKUN-008-UNKNOWN-VLESS-WS-84MS
- AKUN-004-UNKNOWN-VLESS-WS-85MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-UNKNOWN-VLESS-WS-88MS
- AKUN-006-MEDIUM-VLESS-WS-91MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-UNKNOWN-VLESS-WS-93MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
