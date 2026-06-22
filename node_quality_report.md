# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-125MS
- AKUN-006-NET-NL-VLESS-WS-129MS
- AKUN-005-UNKNOWN-VLESS-WS-132MS
- AKUN-002-CLOUDFLARE-VLESS-WS-132MS
- AKUN-004-SPACECORE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-132MS
- AKUN-007-CLOUDFLARE-VLESS-WS-136MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-132MS
- AKUN-010-CLOUDFLARE-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-136MS

## Streaming Pool
- AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-125MS
- AKUN-006-NET-NL-VLESS-WS-129MS
- AKUN-005-UNKNOWN-VLESS-WS-132MS
- AKUN-002-CLOUDFLARE-VLESS-WS-132MS
- AKUN-004-SPACECORE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-132MS
- AKUN-010-CLOUDFLARE-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-136MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-CLOUDFLARE-VLESS-WS-135MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-136MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
