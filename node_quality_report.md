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
- AKUN-003-CLOUDFLARE-VLESS-WS-62MS
- AKUN-001-BIGCOMMERCE-VLESS-WS-65MS
- AKUN-002-ES-FORNEX-20160629-VLESS-WS-65MS
- AKUN-005-UNKNOWN-VLESS-WS-66MS
- AKUN-004-CLOUDFLARE-VLESS-WS-91MS
- AKUN-006-UNKNOWN-VLESS-WS-103MS
- AKUN-007-UNKNOWN-VLESS-WS-111MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-62MS
- AKUN-009-CLOUDFLARE-VLESS-WS-65MS
- AKUN-004-CLOUDFLARE-VLESS-WS-91MS
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS
- AKUN-010-CLOUDFLARE-VLESS-WS-132MS

## Streaming Pool
- AKUN-003-CLOUDFLARE-VLESS-WS-62MS
- AKUN-001-BIGCOMMERCE-VLESS-WS-65MS
- AKUN-002-ES-FORNEX-20160629-VLESS-WS-65MS
- AKUN-009-CLOUDFLARE-VLESS-WS-65MS
- AKUN-005-UNKNOWN-VLESS-WS-66MS
- AKUN-004-CLOUDFLARE-VLESS-WS-91MS
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS
- AKUN-010-CLOUDFLARE-VLESS-WS-132MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-66MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-88MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
