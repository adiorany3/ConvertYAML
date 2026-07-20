# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-005-SAVVY-7-VLESS-WS-60MS
- AKUN-003-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-004-466688-VLESS-WS-69MS
- AKUN-006-US-VLESS-WS-72MS
- AKUN-007-UNKNOWN-VLESS-WS-81MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-003-CLOUDFLARE-VLESS-WS-61MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-005-SAVVY-7-VLESS-WS-60MS
- AKUN-003-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-004-466688-VLESS-WS-69MS
- AKUN-006-US-VLESS-WS-72MS
- AKUN-007-UNKNOWN-VLESS-WS-81MS
- AKUN-008-UNKNOWN-VLESS-WS-90MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
