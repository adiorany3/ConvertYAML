# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-006-CLOUDFLARE-VLESS-WS-58MS
- AKUN-001-DEV-VLESS-WS-59MS
- AKUN-002-UNKNOWN-VLESS-WS-64MS
- AKUN-003-UNKNOWN-VLESS-WS-65MS
- AKUN-004-UNKNOWN-VLESS-WS-70MS
- AKUN-005-ZVC-VLESS-WS-73MS
- AKUN-007-CLOUDFLARE-VLESS-WS-87MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-58MS
- AKUN-001-DEV-VLESS-WS-59MS
- AKUN-010-CLOUDFLARE-VLESS-WS-84MS
- AKUN-007-CLOUDFLARE-VLESS-WS-87MS

## Streaming Pool
- AKUN-006-CLOUDFLARE-VLESS-WS-58MS
- AKUN-001-DEV-VLESS-WS-59MS
- AKUN-002-UNKNOWN-VLESS-WS-64MS
- AKUN-003-UNKNOWN-VLESS-WS-65MS
- AKUN-004-UNKNOWN-VLESS-WS-70MS
- AKUN-005-ZVC-VLESS-WS-73MS
- AKUN-010-CLOUDFLARE-VLESS-WS-84MS
- AKUN-007-CLOUDFLARE-VLESS-WS-87MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-68MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-112MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
