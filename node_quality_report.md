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
- AKUN-002-UNKNOWN-VLESS-WS-70MS
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-UNKNOWN-VLESS-WS-92MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-103MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-005-CLOUDFLARE-VLESS-WS-103MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-70MS
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-003-UNKNOWN-VLESS-WS-92MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-103MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-112MS
- AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-118MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-UNKNOWN-VLESS-WS-110MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
