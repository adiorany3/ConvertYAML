# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS
- AKUN-001-090227-VLESS-WS-65MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS
- AKUN-004-BROADNNET-KR-VLESS-WS-72MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS
- AKUN-007-KIRINO-31-25-88-0-24-VLESS-WS-121MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-93MS

## Streaming Pool
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS
- AKUN-001-090227-VLESS-WS-65MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS
- AKUN-004-BROADNNET-KR-VLESS-WS-72MS
- AKUN-009-CLOUDFLARE-VLESS-WS-93MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS
- AKUN-007-KIRINO-31-25-88-0-24-VLESS-WS-121MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
