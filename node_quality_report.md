# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-CLOUDFLARE-VLESS-WS-300MS
- AKUN-001-HOSTWINDS-17-7-VLESS-WS-302MS
- AKUN-003-ZVC-VLESS-WS-304MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-308MS
- AKUN-004-CLOUDFLARE-VLESS-WS-315MS
- AKUN-006-UNKNOWN-VLESS-WS-317MS
- AKUN-007-CLOUDFLARE-VLESS-WS-323MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-300MS
- AKUN-004-CLOUDFLARE-VLESS-WS-315MS
- AKUN-007-CLOUDFLARE-VLESS-WS-323MS

## Streaming Pool
- AKUN-002-CLOUDFLARE-VLESS-WS-300MS
- AKUN-001-HOSTWINDS-17-7-VLESS-WS-302MS
- AKUN-003-ZVC-VLESS-WS-304MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-308MS
- AKUN-004-CLOUDFLARE-VLESS-WS-315MS
- AKUN-006-UNKNOWN-VLESS-WS-317MS
- AKUN-007-CLOUDFLARE-VLESS-WS-323MS
- AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-328MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
