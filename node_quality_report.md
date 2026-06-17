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
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-007-CLOUDFLARE-VLESS-WS-82MS
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS
- AKUN-006-CLOUDFLARE-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-004-CLOUDFLARE-VLESS-WS-100MS
- AKUN-005-CLOUDFLARE-VLESS-WS-125MS

## Tier 1B - WARM-UP-CF
- AKUN-007-CLOUDFLARE-VLESS-WS-82MS
- AKUN-006-CLOUDFLARE-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-004-CLOUDFLARE-VLESS-WS-100MS
- AKUN-005-CLOUDFLARE-VLESS-WS-125MS

## Streaming Pool
- AKUN-007-CLOUDFLARE-VLESS-WS-82MS
- AKUN-006-CLOUDFLARE-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-004-CLOUDFLARE-VLESS-WS-100MS
- AKUN-005-CLOUDFLARE-VLESS-WS-125MS
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS
- AKUN-008-CLOUDFLARE-VLESS-WS-238MS

## AUTO-FAST Pool
- AKUN-007-CLOUDFLARE-VLESS-WS-82MS
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-86MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-92MS
- AKUN-006-CLOUDFLARE-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-004-CLOUDFLARE-VLESS-WS-100MS
- AKUN-005-CLOUDFLARE-VLESS-WS-125MS
- AKUN-008-CLOUDFLARE-VLESS-WS-238MS
- AKUN-009-CLOUDFLARE-VLESS-WS-243MS
- AKUN-010-UNKNOWN-VLESS-WS-276MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-CLOUDFLARE-VLESS-WS-128MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-DEV-VLESS-WS-126MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-128MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-92MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-UNKNOWN-VLESS-WS-97MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
