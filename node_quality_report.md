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
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS
- AKUN-006-CLOUDFLARE-VLESS-WS-91MS
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS
- AKUN-002-CLOUDFLARE-VLESS-WS-98MS
- AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-100MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-91MS
- AKUN-002-CLOUDFLARE-VLESS-WS-98MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-008-CLOUDFLARE-VLESS-WS-114MS
- AKUN-010-CLOUDFLARE-VLESS-WS-118MS

## Streaming Pool
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS
- AKUN-006-CLOUDFLARE-VLESS-WS-91MS
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-94MS
- AKUN-002-CLOUDFLARE-VLESS-WS-98MS
- AKUN-003-GO-DADDY-COM-LLC-VLESS-WS-100MS
- AKUN-004-CLOUDFLARE-VLESS-WS-109MS
- AKUN-008-CLOUDFLARE-VLESS-WS-114MS
- AKUN-010-CLOUDFLARE-VLESS-WS-118MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-UNKNOWN-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-DEV-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-122MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
