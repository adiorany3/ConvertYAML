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
- AKUN-006-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-CLOUDFLARE-VLESS-WS-78MS
- AKUN-001-BIGCOMMERCE-VLESS-WS-84MS
- AKUN-002-ORACLE-VLESS-WS-88MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-007-CLOUDFLARE-VLESS-WS-98MS
- AKUN-005-CLOUDFLARE-VLESS-WS-108MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-CLOUDFLARE-VLESS-WS-78MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-007-CLOUDFLARE-VLESS-WS-98MS
- AKUN-005-CLOUDFLARE-VLESS-WS-108MS

## Streaming Pool
- AKUN-006-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-CLOUDFLARE-VLESS-WS-78MS
- AKUN-001-BIGCOMMERCE-VLESS-WS-84MS
- AKUN-002-ORACLE-VLESS-WS-88MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-007-CLOUDFLARE-VLESS-WS-98MS
- AKUN-008-UNKNOWN-VLESS-WS-103MS
- AKUN-005-CLOUDFLARE-VLESS-WS-108MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-002-CLOUDFLARE-VLESS-WS-69MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-95MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-DEV-VLESS-WS-99MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-97MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
