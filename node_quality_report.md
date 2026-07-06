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
- AKUN-004-WPENG-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-65MS
- AKUN-001-OVH-VLESS-WS-66MS
- AKUN-002-CLOUDFLARE-VLESS-WS-71MS
- AKUN-005-CLOUDFLARE-VLESS-WS-77MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-007-CHSL-HEL-VLESS-WS-97MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-65MS
- AKUN-002-CLOUDFLARE-VLESS-WS-71MS
- AKUN-005-CLOUDFLARE-VLESS-WS-77MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS

## Streaming Pool
- AKUN-004-WPENG-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-65MS
- AKUN-001-OVH-VLESS-WS-66MS
- AKUN-002-CLOUDFLARE-VLESS-WS-71MS
- AKUN-005-CLOUDFLARE-VLESS-WS-77MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS
- AKUN-007-CHSL-HEL-VLESS-WS-97MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
