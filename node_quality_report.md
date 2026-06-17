# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 18
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 18 referensi, manual backup: 8 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS
- AKUN-001-NEXUSMODS-VLESS-WS-93MS
- AKUN-003-CLOUDFLARE-VLESS-WS-98MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS
- AKUN-006-CLOUDFLARE-VLESS-WS-110MS
- AKUN-007-UNKNOWN-VLESS-WS-110MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-98MS
- AKUN-010-CLOUDFLARE-VLESS-WS-102MS
- AKUN-006-CLOUDFLARE-VLESS-WS-110MS
- AKUN-008-CLOUDFLARE-VLESS-WS-120MS
- AKUN-009-CLOUDFLARE-VLESS-WS-138MS

## Streaming Pool
- AKUN-001-NEXUSMODS-VLESS-WS-93MS
- AKUN-003-CLOUDFLARE-VLESS-WS-98MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS
- AKUN-010-CLOUDFLARE-VLESS-WS-102MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS
- AKUN-006-CLOUDFLARE-VLESS-WS-110MS
- AKUN-008-CLOUDFLARE-VLESS-WS-120MS
- AKUN-009-CLOUDFLARE-VLESS-WS-138MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-CLOUDFLARE-VLESS-WS-115MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-118MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-115MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-131MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-111MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-111MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-CLOUDFLARE-VLESS-WS-141MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
