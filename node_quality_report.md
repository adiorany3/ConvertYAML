# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-MVPS-NET-VLESS-WS-75MS
- AKUN-002-UNKNOWN-VLESS-WS-81MS
- AKUN-004-UNKNOWN-VLESS-WS-83MS
- AKUN-006-OPENAI-VLESS-WS-87MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS
- AKUN-003-UNKNOWN-VLESS-WS-97MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-73MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS

## Streaming Pool
- AKUN-008-CLOUDFLARE-VLESS-WS-73MS
- AKUN-001-MVPS-NET-VLESS-WS-75MS
- AKUN-002-UNKNOWN-VLESS-WS-81MS
- AKUN-004-UNKNOWN-VLESS-WS-83MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS
- AKUN-003-UNKNOWN-VLESS-WS-97MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
