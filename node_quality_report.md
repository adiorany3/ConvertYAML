# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-57MS
- AKUN-001-UNKNOWN-VLESS-WS-62MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-004-BROADNNET-KR-VLESS-WS-94MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-105MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-010-CLOUDFLARE-VLESS-WS-82MS
- AKUN-008-CLOUDFLARE-VLESS-WS-94MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS

## Streaming Pool
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-57MS
- AKUN-001-UNKNOWN-VLESS-WS-62MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-69MS
- AKUN-003-CLOUDFLARE-VLESS-WS-76MS
- AKUN-010-CLOUDFLARE-VLESS-WS-82MS
- AKUN-004-BROADNNET-KR-VLESS-WS-94MS
- AKUN-008-CLOUDFLARE-VLESS-WS-94MS
- AKUN-005-CLOUDFLARE-VLESS-WS-99MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-DEV-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-87MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-85MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-125MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-88MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
