# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-102MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-117MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-008-CLOUDFLARE-VLESS-WS-94MS
- AKUN-006-CLOUDFLARE-VLESS-WS-102MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-78MS
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-008-CLOUDFLARE-VLESS-WS-94MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-102MS
- AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-117MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-91MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-124MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-SPEEDTEST-VLESS-WS-180MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
