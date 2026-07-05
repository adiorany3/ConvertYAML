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
- AKUN-001-OVH-VLESS-WS-56MS
- AKUN-006-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-005-ZVC-VLESS-WS-68MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS

## Streaming Pool
- AKUN-001-OVH-VLESS-WS-56MS
- AKUN-006-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-008-CLOUDFLARE-VLESS-WS-65MS
- AKUN-005-ZVC-VLESS-WS-68MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CHSL-HEL-VLESS-WS-64MS: ProxyError: HTTPSConnectionPool(host='www.gstatic.com', port=443): Max retries exceeded with url: /generate_204 (Caused by ProxyError('Unable to connect
- AKUN-011-CLOUDFLARE-VLESS-WS-89MS: SSLError: HTTPSConnectionPool(host='www.gstatic.com', port=443): Max retries exceeded with url: /generate_204 (Caused by SSLError(SSLEOFError(8, '[SSL

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
