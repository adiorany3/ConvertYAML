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
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-002-UNKNOWN-VLESS-WS-83MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS
- AKUN-005-CLOUDFLARE-VLESS-WS-118MS
- AKUN-007-CLOUDFLARE-VLESS-WS-138MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-008-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-005-CLOUDFLARE-VLESS-WS-118MS
- AKUN-007-CLOUDFLARE-VLESS-WS-138MS

## Streaming Pool
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS
- AKUN-001-CLOUDFLARE-VLESS-WS-75MS
- AKUN-008-CLOUDFLARE-VLESS-WS-81MS
- AKUN-002-UNKNOWN-VLESS-WS-83MS
- AKUN-006-CLOUDFLARE-VLESS-WS-87MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS
- AKUN-005-CLOUDFLARE-VLESS-WS-118MS
- AKUN-007-CLOUDFLARE-VLESS-WS-138MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-DEV-VLESS-WS-79MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-94MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-78MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-72MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-110MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-UNKNOWN-VLESS-WS-101MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-79MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-DEV-VLESS-WS-112MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-018-CLOUDFLARE-VLESS-WS-98MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
