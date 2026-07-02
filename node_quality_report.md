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
- AKUN-004-VULTR-VLESS-WS-63MS
- AKUN-002-CLOUDFLARE-VLESS-WS-66MS
- AKUN-001-CLOUDFLARE-VLESS-WS-67MS
- AKUN-005-CLOUDFLARE-VLESS-WS-73MS
- AKUN-003-AEZA-NETWORK-VLESS-WS-73MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-007-COMPREND-NET-VLESS-WS-90MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-66MS
- AKUN-001-CLOUDFLARE-VLESS-WS-67MS
- AKUN-005-CLOUDFLARE-VLESS-WS-73MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS

## Streaming Pool
- AKUN-004-VULTR-VLESS-WS-63MS
- AKUN-002-CLOUDFLARE-VLESS-WS-66MS
- AKUN-001-CLOUDFLARE-VLESS-WS-67MS
- AKUN-005-CLOUDFLARE-VLESS-WS-73MS
- AKUN-003-AEZA-NETWORK-VLESS-WS-73MS
- AKUN-008-COMPREND-NET-VLESS-WS-84MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-007-COMPREND-NET-VLESS-WS-90MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
