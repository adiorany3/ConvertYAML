# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-006-WPENG-VLESS-WS-67MS
- AKUN-001-VULTR-VLESS-WS-70MS
- AKUN-004-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-COMPREND-NET-VLESS-WS-79MS
- AKUN-007-466688-VLESS-WS-79MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-010-CLOUDFLARE-VLESS-WS-78MS

## Streaming Pool
- AKUN-006-WPENG-VLESS-WS-67MS
- AKUN-001-VULTR-VLESS-WS-70MS
- AKUN-004-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-010-CLOUDFLARE-VLESS-WS-78MS
- AKUN-005-COMPREND-NET-VLESS-WS-79MS
- AKUN-007-466688-VLESS-WS-79MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
