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
- AKUN-001-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-UNKNOWN-VLESS-WS-105MS
- AKUN-002-CLOUDFLARE-VLESS-WS-111MS
- AKUN-003-UNKNOWN-VLESS-WS-113MS
- AKUN-004-MEDIUM-VLESS-WS-114MS
- AKUN-007-UNKNOWN-VLESS-WS-126MS
- AKUN-005-466688-VLESS-WS-126MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-87MS
- AKUN-010-CLOUDFLARE-VLESS-WS-105MS
- AKUN-002-CLOUDFLARE-VLESS-WS-111MS
- AKUN-009-CLOUDFLARE-VLESS-WS-120MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-UNKNOWN-VLESS-WS-105MS
- AKUN-010-CLOUDFLARE-VLESS-WS-105MS
- AKUN-002-CLOUDFLARE-VLESS-WS-111MS
- AKUN-003-UNKNOWN-VLESS-WS-113MS
- AKUN-004-MEDIUM-VLESS-WS-114MS
- AKUN-009-CLOUDFLARE-VLESS-WS-120MS
- AKUN-005-466688-VLESS-WS-126MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
