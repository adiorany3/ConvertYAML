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
- AKUN-001-466688-VLESS-WS-72MS
- AKUN-002-NETCRAFTERS-VLESS-WS-74MS
- AKUN-004-COMPREND-NET-VLESS-WS-75MS
- AKUN-006-CLOUDFLARE-VLESS-WS-79MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-005-466688-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-147MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-79MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-007-CLOUDFLARE-VLESS-WS-147MS
- AKUN-009-DEV-VLESS-WS-187MS
- AKUN-010-CLOUDFLARE-VLESS-WS-262MS

## Streaming Pool
- AKUN-001-466688-VLESS-WS-72MS
- AKUN-002-NETCRAFTERS-VLESS-WS-74MS
- AKUN-004-COMPREND-NET-VLESS-WS-75MS
- AKUN-006-CLOUDFLARE-VLESS-WS-79MS
- AKUN-003-CLOUDFLARE-VLESS-WS-91MS
- AKUN-007-CLOUDFLARE-VLESS-WS-147MS
- AKUN-009-DEV-VLESS-WS-187MS
- AKUN-010-CLOUDFLARE-VLESS-WS-262MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-72MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
