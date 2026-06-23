# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-89MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-102MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-007-CLOUDFLARE-VLESS-WS-145MS
- AKUN-006-BROADNNET-KR-VLESS-WS-147MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-007-CLOUDFLARE-VLESS-WS-145MS
- AKUN-010-CLOUDFLARE-VLESS-WS-303MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-89MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-102MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-007-CLOUDFLARE-VLESS-WS-145MS
- AKUN-006-BROADNNET-KR-VLESS-WS-147MS
- AKUN-010-CLOUDFLARE-VLESS-WS-303MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-CLOUDFLARE-VLESS-WS-89MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-DEV-VLESS-WS-94MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-DEV-VLESS-WS-123MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
