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
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-110MS
- AKUN-002-CLOUDFLARE-VLESS-WS-114MS
- AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-121MS
- AKUN-007-ZOOM-VLESS-WS-128MS
- AKUN-003-CLOUDFLARE-VLESS-WS-134MS
- AKUN-005-COMPREND-NET-VLESS-WS-137MS
- AKUN-006-COMPREND-NET-VLESS-WS-144MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-114MS
- AKUN-003-CLOUDFLARE-VLESS-WS-134MS
- AKUN-010-CLOUDFLARE-VLESS-WS-154MS

## Streaming Pool
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-110MS
- AKUN-002-CLOUDFLARE-VLESS-WS-114MS
- AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-121MS
- AKUN-007-ZOOM-VLESS-WS-128MS
- AKUN-003-CLOUDFLARE-VLESS-WS-134MS
- AKUN-005-COMPREND-NET-VLESS-WS-137MS
- AKUN-006-COMPREND-NET-VLESS-WS-144MS
- AKUN-010-CLOUDFLARE-VLESS-WS-154MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
