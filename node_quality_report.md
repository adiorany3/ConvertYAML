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
- AKUN-001-UNKNOWN-VLESS-WS-81MS
- AKUN-003-BGP48-HK-VLESS-WS-85MS
- AKUN-004-UNKNOWN-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-104MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS
- AKUN-002-154-197-64-0-154-197-64-VLESS-WS-111MS
- AKUN-005-BGP48-HK-VLESS-WS-112MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-104MS
- AKUN-009-CLOUDFLARE-VLESS-WS-122MS
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-81MS
- AKUN-003-BGP48-HK-VLESS-WS-85MS
- AKUN-004-UNKNOWN-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-104MS
- AKUN-002-154-197-64-0-154-197-64-VLESS-WS-111MS
- AKUN-005-BGP48-HK-VLESS-WS-112MS
- AKUN-009-CLOUDFLARE-VLESS-WS-122MS
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
