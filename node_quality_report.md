# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-UNKNOWN-VLESS-WS-112MS
- AKUN-001-UNKNOWN-VLESS-WS-113MS
- AKUN-005-CLOUDFLARE-VLESS-WS-114MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-115MS
- AKUN-003-UNKNOWN-VLESS-WS-116MS
- AKUN-004-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-114MS
- AKUN-008-CLOUDFLARE-VLESS-WS-116MS
- AKUN-004-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS
- AKUN-010-CLOUDFLARE-VLESS-WS-129MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-112MS
- AKUN-001-UNKNOWN-VLESS-WS-113MS
- AKUN-005-CLOUDFLARE-VLESS-WS-114MS
- AKUN-008-CLOUDFLARE-VLESS-WS-116MS
- AKUN-003-UNKNOWN-VLESS-WS-116MS
- AKUN-004-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS
- AKUN-010-CLOUDFLARE-VLESS-WS-129MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
