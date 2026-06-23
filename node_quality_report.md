# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-003-UNKNOWN-VLESS-WS-72MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS
- AKUN-005-BROADNNET-KR-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-85MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-95MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-85MS

## Streaming Pool
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-59MS
- AKUN-002-UNKNOWN-VLESS-WS-63MS
- AKUN-003-UNKNOWN-VLESS-WS-72MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS
- AKUN-005-BROADNNET-KR-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-85MS
- AKUN-008-BROADNNET-KR-VLESS-WS-86MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-95MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-DEV-VLESS-WS-71MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-69MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-72MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-114MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
