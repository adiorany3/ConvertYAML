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
- AKUN-001-ORACLE-VLESS-WS-74MS
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-83MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-83MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-87MS
- AKUN-008-CLOUDFLARE-VLESS-WS-145MS

## Streaming Pool
- AKUN-001-ORACLE-VLESS-WS-74MS
- AKUN-005-CLOUDFLARE-VLESS-WS-75MS
- AKUN-004-CLOUDFLARE-VLESS-WS-83MS
- AKUN-002-CLOUDFLARE-VLESS-WS-85MS
- AKUN-003-CLOUDFLARE-VLESS-WS-87MS
- AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-105MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS
- AKUN-008-CLOUDFLARE-VLESS-WS-145MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-CLOUDFLARE-VLESS-WS-107MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-DEV-VLESS-WS-98MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-120MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-DEV-VLESS-WS-138MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-DEV-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-DEV-VLESS-WS-136MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
