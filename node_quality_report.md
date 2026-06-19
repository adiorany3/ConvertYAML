# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-007-UNKNOWN-VLESS-WS-100MS
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-108MS
- AKUN-005-UNKNOWN-VLESS-WS-112MS
- AKUN-002-VULTR-VLESS-WS-122MS
- AKUN-004-MEDIUM-VLESS-WS-129MS
- AKUN-006-UNKNOWN-VLESS-WS-141MS
- AKUN-003-CLOUDFLARE-VLESS-WS-144MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS
- AKUN-003-CLOUDFLARE-VLESS-WS-144MS
- AKUN-009-CLOUDFLARE-VLESS-WS-144MS

## Streaming Pool
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-108MS
- AKUN-005-UNKNOWN-VLESS-WS-112MS
- AKUN-002-VULTR-VLESS-WS-122MS
- AKUN-008-CLOUDFLARE-VLESS-WS-126MS
- AKUN-004-MEDIUM-VLESS-WS-129MS
- AKUN-006-UNKNOWN-VLESS-WS-141MS
- AKUN-003-CLOUDFLARE-VLESS-WS-144MS
- AKUN-009-CLOUDFLARE-VLESS-WS-144MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-DEV-VLESS-WS-153MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
