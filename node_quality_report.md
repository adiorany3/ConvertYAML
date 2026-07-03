# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS
- AKUN-002-WPENG-VLESS-WS-78MS
- AKUN-005-WEYRO-NET-VLESS-WS-78MS
- AKUN-007-COMPREND-NET-VLESS-WS-100MS
- AKUN-006-WPENG-VLESS-WS-106MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-72MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS
- AKUN-010-CLOUDFLARE-VLESS-WS-104MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS
- AKUN-002-WPENG-VLESS-WS-78MS
- AKUN-005-WEYRO-NET-VLESS-WS-78MS
- AKUN-007-COMPREND-NET-VLESS-WS-100MS
- AKUN-010-CLOUDFLARE-VLESS-WS-104MS
- AKUN-006-WPENG-VLESS-WS-106MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
