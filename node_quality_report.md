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
- AKUN-001-9889888-VLESS-WS-70MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS
- AKUN-003-CLOUDFLARE-VLESS-WS-107MS
- AKUN-007-UNKNOWN-VLESS-WS-370MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS
- AKUN-003-CLOUDFLARE-VLESS-WS-107MS

## Streaming Pool
- AKUN-008-UNKNOWN-VLESS-WS-69MS
- AKUN-001-9889888-VLESS-WS-70MS
- AKUN-002-CLOUDFLARE-VLESS-WS-76MS
- AKUN-005-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-83MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS
- AKUN-003-CLOUDFLARE-VLESS-WS-107MS
- AKUN-007-UNKNOWN-VLESS-WS-370MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-90MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-98MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-410MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
