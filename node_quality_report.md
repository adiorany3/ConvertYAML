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
- AKUN-001-UNKNOWN-VLESS-WS-56MS
- AKUN-005-UNKNOWN-VLESS-WS-56MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-006-CLOUDFLARE-VLESS-WS-64MS
- AKUN-003-UNKNOWN-VLESS-WS-65MS
- AKUN-004-ZENFO-1-VLESS-WS-67MS
- AKUN-007-CLOUDFLARE-VLESS-WS-69MS

## Tier 1B - WARM-UP-CF
- AKUN-010-CLOUDFLARE-VLESS-WS-56MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-006-CLOUDFLARE-VLESS-WS-64MS
- AKUN-007-CLOUDFLARE-VLESS-WS-69MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-56MS
- AKUN-005-UNKNOWN-VLESS-WS-56MS
- AKUN-010-CLOUDFLARE-VLESS-WS-56MS
- AKUN-002-CLOUDFLARE-VLESS-WS-62MS
- AKUN-006-CLOUDFLARE-VLESS-WS-64MS
- AKUN-003-UNKNOWN-VLESS-WS-65MS
- AKUN-004-ZENFO-1-VLESS-WS-67MS
- AKUN-007-CLOUDFLARE-VLESS-WS-69MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-006-NOTION-WEB-VLESS-WS-63MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-011-CLOUDFLARE-VLESS-WS-66MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
