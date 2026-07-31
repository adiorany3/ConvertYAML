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
- AKUN-006-CLOUDFLARE-VLESS-WS-133MS
- AKUN-003-OVH-VLESS-WS-135MS
- AKUN-001-CLOUDFLARE-VLESS-WS-139MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-139MS
- AKUN-002-CLOUDFLARE-VLESS-WS-141MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-149MS
- AKUN-007-UNKNOWN-VLESS-WS-152MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-133MS
- AKUN-009-CLOUDFLARE-VLESS-WS-134MS
- AKUN-008-CLOUDFLARE-VLESS-WS-138MS
- AKUN-001-CLOUDFLARE-VLESS-WS-139MS
- AKUN-002-CLOUDFLARE-VLESS-WS-141MS

## Streaming Pool
- AKUN-006-CLOUDFLARE-VLESS-WS-133MS
- AKUN-009-CLOUDFLARE-VLESS-WS-134MS
- AKUN-003-OVH-VLESS-WS-135MS
- AKUN-008-CLOUDFLARE-VLESS-WS-138MS
- AKUN-001-CLOUDFLARE-VLESS-WS-139MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-139MS
- AKUN-002-CLOUDFLARE-VLESS-WS-141MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-149MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-126MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-137MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-129MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
