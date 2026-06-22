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
- AKUN-001-090227-VLESS-WS-63MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS
- AKUN-007-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-006-CLOUDFLARE-VLESS-WS-82MS
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-75MS
- AKUN-007-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-006-CLOUDFLARE-VLESS-WS-82MS
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS

## Streaming Pool
- AKUN-001-090227-VLESS-WS-63MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS
- AKUN-009-CLOUDFLARE-VLESS-WS-75MS
- AKUN-007-CLOUDFLARE-VLESS-WS-79MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-006-CLOUDFLARE-VLESS-WS-82MS
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-CLOUDFLARE-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-127MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-124MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-122MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-SPEEDTEST-VLESS-WS-123MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-SPEEDTEST-VLESS-WS-158MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
