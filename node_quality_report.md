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
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-1PASSWORD-VLESS-WS-70MS
- AKUN-003-UNKNOWN-VLESS-WS-71MS
- AKUN-007-LEVIKOGJGFDD-VLESS-WS-71MS
- AKUN-001-UNKNOWN-VLESS-WS-73MS
- AKUN-006-ADF-VLESS-WS-76MS
- AKUN-005-ZVC-VLESS-WS-78MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-008-CLOUDFLARE-VLESS-WS-71MS
- AKUN-009-CLOUDFLARE-VLESS-WS-73MS
- AKUN-010-CLOUDFLARE-VLESS-WS-89MS

## Streaming Pool
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-1PASSWORD-VLESS-WS-70MS
- AKUN-003-UNKNOWN-VLESS-WS-71MS
- AKUN-008-CLOUDFLARE-VLESS-WS-71MS
- AKUN-001-UNKNOWN-VLESS-WS-73MS
- AKUN-009-CLOUDFLARE-VLESS-WS-73MS
- AKUN-005-ZVC-VLESS-WS-78MS
- AKUN-010-CLOUDFLARE-VLESS-WS-89MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-UNKNOWN-VLESS-WS-73MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
