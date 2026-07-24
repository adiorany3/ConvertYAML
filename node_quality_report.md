# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-003-UNKNOWN-VLESS-WS-60MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-001-ZVC-VLESS-WS-65MS
- AKUN-004-CLOUDFLARE-VLESS-WS-69MS
- AKUN-006-CLOUDFLARE-VLESS-WS-70MS
- AKUN-005-UNKNOWN-VLESS-WS-72MS
- AKUN-007-UNKNOWN-VLESS-WS-73MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-69MS
- AKUN-006-CLOUDFLARE-VLESS-WS-70MS
- AKUN-010-CLOUDFLARE-VLESS-WS-90MS

## Streaming Pool
- AKUN-003-UNKNOWN-VLESS-WS-60MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-001-ZVC-VLESS-WS-65MS
- AKUN-004-CLOUDFLARE-VLESS-WS-69MS
- AKUN-006-CLOUDFLARE-VLESS-WS-70MS
- AKUN-005-UNKNOWN-VLESS-WS-72MS
- AKUN-007-UNKNOWN-VLESS-WS-73MS
- AKUN-010-CLOUDFLARE-VLESS-WS-90MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
