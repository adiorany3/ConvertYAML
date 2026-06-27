# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-466688-VLESS-WS-79MS
- AKUN-003-UNKNOWN-VLESS-WS-85MS
- AKUN-004-UNKNOWN-VLESS-WS-91MS
- AKUN-006-CLOUDFLARE-VLESS-WS-94MS
- AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-116MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-006-CLOUDFLARE-VLESS-WS-94MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-75MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-466688-VLESS-WS-79MS
- AKUN-003-UNKNOWN-VLESS-WS-85MS
- AKUN-004-UNKNOWN-VLESS-WS-91MS
- AKUN-006-CLOUDFLARE-VLESS-WS-94MS
- AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-116MS
- AKUN-008-DE-XTOM-20210903-VLESS-WS-121MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
