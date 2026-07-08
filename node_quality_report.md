# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-ZVC-VLESS-WS-77MS
- AKUN-005-WPENG-VLESS-WS-79MS
- AKUN-002-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-003-CLOUDFLARE-VLESS-WS-86MS
- AKUN-007-UNKNOWN-VLESS-WS-90MS
- AKUN-006-WPENG-VLESS-WS-97MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-003-CLOUDFLARE-VLESS-WS-86MS
- AKUN-010-CLOUDFLARE-VLESS-WS-92MS
- AKUN-009-CLOUDFLARE-VLESS-WS-95MS

## Streaming Pool
- AKUN-001-ZVC-VLESS-WS-77MS
- AKUN-005-WPENG-VLESS-WS-79MS
- AKUN-002-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-86MS
- AKUN-003-CLOUDFLARE-VLESS-WS-86MS
- AKUN-010-CLOUDFLARE-VLESS-WS-92MS
- AKUN-009-CLOUDFLARE-VLESS-WS-95MS
- AKUN-006-WPENG-VLESS-WS-97MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
