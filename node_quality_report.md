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
- AKUN-001-ZVC-VLESS-WS-83MS
- AKUN-003-CLOUDFLARE-VLESS-WS-90MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-006-TANG-NET-VLESS-WS-94MS
- AKUN-004-CLOUDFLARE-VLESS-WS-95MS
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-007-UNKNOWN-VLESS-WS-259MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-90MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-004-CLOUDFLARE-VLESS-WS-95MS
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-008-CLOUDFLARE-VLESS-WS-268MS

## Streaming Pool
- AKUN-001-ZVC-VLESS-WS-83MS
- AKUN-003-CLOUDFLARE-VLESS-WS-90MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-006-TANG-NET-VLESS-WS-94MS
- AKUN-004-CLOUDFLARE-VLESS-WS-95MS
- AKUN-005-CLOUDFLARE-VLESS-WS-116MS
- AKUN-007-UNKNOWN-VLESS-WS-259MS
- AKUN-008-CLOUDFLARE-VLESS-WS-268MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-86MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-106MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-99MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-UNKNOWN-VLESS-WS-267MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
