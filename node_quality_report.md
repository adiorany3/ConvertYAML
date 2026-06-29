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
- AKUN-002-UNKNOWN-VLESS-WS-99MS
- AKUN-001-MYBB-VLESS-WS-107MS
- AKUN-004-US-VLESS-WS-109MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS
- AKUN-003-CLOUDFLARE-VLESS-WS-115MS
- AKUN-005-UNKNOWN-VLESS-WS-121MS
- AKUN-006-CLOUDFLARE-VLESS-WS-124MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-115MS
- AKUN-009-CLOUDFLARE-VLESS-WS-118MS
- AKUN-010-CLOUDFLARE-VLESS-WS-120MS
- AKUN-006-CLOUDFLARE-VLESS-WS-124MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-99MS
- AKUN-001-MYBB-VLESS-WS-107MS
- AKUN-004-US-VLESS-WS-109MS
- AKUN-003-CLOUDFLARE-VLESS-WS-115MS
- AKUN-009-CLOUDFLARE-VLESS-WS-118MS
- AKUN-010-CLOUDFLARE-VLESS-WS-120MS
- AKUN-005-UNKNOWN-VLESS-WS-121MS
- AKUN-006-CLOUDFLARE-VLESS-WS-124MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
