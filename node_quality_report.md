# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 15
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 15 referensi, manual backup: 5 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-ZVC-VLESS-WS-76MS
- AKUN-002-GOOGLE-VLESS-WS-84MS
- AKUN-006-ZVC-VLESS-WS-91MS
- AKUN-003-UNKNOWN-VLESS-WS-96MS
- AKUN-004-3666888-VLESS-WS-97MS
- AKUN-005-UNKNOWN-VLESS-WS-105MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-122MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS
- AKUN-009-CLOUDFLARE-VLESS-WS-151MS
- AKUN-010-CLOUDFLARE-VLESS-WS-184MS

## Streaming Pool
- AKUN-001-ZVC-VLESS-WS-76MS
- AKUN-002-GOOGLE-VLESS-WS-84MS
- AKUN-003-UNKNOWN-VLESS-WS-96MS
- AKUN-004-3666888-VLESS-WS-97MS
- AKUN-008-CLOUDFLARE-VLESS-WS-122MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS
- AKUN-009-CLOUDFLARE-VLESS-WS-151MS
- AKUN-010-CLOUDFLARE-VLESS-WS-184MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-008-CLOUDFLARE-VLESS-WS-114MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-96MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-105MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-161MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
