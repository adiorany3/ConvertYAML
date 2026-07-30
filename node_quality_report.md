# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-004-ZVC-VLESS-WS-83MS
- AKUN-006-UNKNOWN-VLESS-WS-84MS
- AKUN-001-DEV-VLESS-WS-85MS
- AKUN-002-UNKNOWN-VLESS-WS-89MS
- AKUN-003-DEV-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-007-CHATGPT-VLESS-WS-95MS

## Tier 1B - WARM-UP-CF
- AKUN-001-DEV-VLESS-WS-85MS
- AKUN-008-CLOUDFLARE-VLESS-WS-88MS
- AKUN-003-DEV-VLESS-WS-89MS
- AKUN-009-CLOUDFLARE-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS

## Streaming Pool
- AKUN-004-ZVC-VLESS-WS-83MS
- AKUN-006-UNKNOWN-VLESS-WS-84MS
- AKUN-001-DEV-VLESS-WS-85MS
- AKUN-008-CLOUDFLARE-VLESS-WS-88MS
- AKUN-002-UNKNOWN-VLESS-WS-89MS
- AKUN-003-DEV-VLESS-WS-89MS
- AKUN-009-CLOUDFLARE-VLESS-WS-89MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-87MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
