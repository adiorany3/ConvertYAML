# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-ALIBABA-VLESS-WS-64MS
- AKUN-004-CLOUDFLARE-VLESS-WS-72MS
- AKUN-005-WPENG-VLESS-WS-78MS
- AKUN-003-CLOUDFLARE-VLESS-WS-80MS
- AKUN-002-DIGITALOCEAN-VLESS-WS-81MS
- AKUN-006-DIGITALOCEAN-VLESS-WS-83MS
- AKUN-007-DIGITALOCEAN-VLESS-WS-87MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-CLOUDFLARE-VLESS-WS-80MS

## Streaming Pool
- AKUN-001-ALIBABA-VLESS-WS-64MS
- AKUN-004-CLOUDFLARE-VLESS-WS-72MS
- AKUN-005-WPENG-VLESS-WS-78MS
- AKUN-003-CLOUDFLARE-VLESS-WS-80MS
- AKUN-002-DIGITALOCEAN-VLESS-WS-81MS
- AKUN-006-DIGITALOCEAN-VLESS-WS-83MS
- AKUN-008-COMPREND-NET-VLESS-WS-83MS
- AKUN-007-DIGITALOCEAN-VLESS-WS-87MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-95MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
