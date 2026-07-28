# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-126MS
- AKUN-002-UNKNOWN-VLESS-WS-130MS
- AKUN-003-UNKNOWN-VLESS-WS-146MS
- AKUN-006-CLOUDFLARE-VLESS-WS-146MS
- AKUN-004-UNKNOWN-VLESS-WS-156MS
- AKUN-007-SKK-VLESS-WS-177MS
- AKUN-005-CLOUDFLARE-VLESS-WS-186MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-146MS
- AKUN-005-CLOUDFLARE-VLESS-WS-186MS
- AKUN-008-CLOUDFLARE-VLESS-WS-236MS
- AKUN-009-CLOUDFLARE-VLESS-WS-290MS
- AKUN-010-CLOUDFLARE-VLESS-WS-305MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-126MS
- AKUN-002-UNKNOWN-VLESS-WS-130MS
- AKUN-003-UNKNOWN-VLESS-WS-146MS
- AKUN-006-CLOUDFLARE-VLESS-WS-146MS
- AKUN-005-CLOUDFLARE-VLESS-WS-186MS
- AKUN-008-CLOUDFLARE-VLESS-WS-236MS
- AKUN-009-CLOUDFLARE-VLESS-WS-290MS
- AKUN-010-CLOUDFLARE-VLESS-WS-305MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-UNKNOWN-VLESS-WS-115MS: SSLError: HTTPSConnectionPool(host='www.gstatic.com', port=443): Max retries exceeded with url: /generate_204 (Caused by SSLError(SSLEOFError(8, '[SSL
- AKUN-008-CLOUDFLARE-VLESS-WS-177MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-161MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
