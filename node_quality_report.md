# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 18
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 18 referensi, manual backup: 8 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDBACKBONE-VLESS-WS-80MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS
- AKUN-005-EU-VLESS-WS-98MS
- AKUN-002-NETCUP-VLESS-WS-98MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS
- AKUN-006-SPACECORE-VLESS-WS-103MS
- AKUN-004-DIGITALOCEAN-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-113MS

## Streaming Pool
- AKUN-001-CLOUDBACKBONE-VLESS-WS-80MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS
- AKUN-005-EU-VLESS-WS-98MS
- AKUN-002-NETCUP-VLESS-WS-98MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS
- AKUN-006-SPACECORE-VLESS-WS-103MS
- AKUN-004-DIGITALOCEAN-VLESS-WS-107MS
- AKUN-009-CLOUDFLARE-VLESS-WS-113MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
