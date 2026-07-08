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
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-005-ZVC-VLESS-WS-65MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-ES-FORNEX-20160629-VLESS-WS-83MS
- AKUN-006-OVH-VLESS-WS-85MS
- AKUN-004-CLOUDFLARE-VLESS-WS-88MS
- AKUN-007-UNKNOWN-VLESS-WS-117MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-004-CLOUDFLARE-VLESS-WS-88MS
- AKUN-008-CLOUDFLARE-VLESS-WS-120MS
- AKUN-009-CLOUDFLARE-VLESS-WS-131MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-005-ZVC-VLESS-WS-65MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-003-ES-FORNEX-20160629-VLESS-WS-83MS
- AKUN-006-OVH-VLESS-WS-85MS
- AKUN-004-CLOUDFLARE-VLESS-WS-88MS
- AKUN-008-CLOUDFLARE-VLESS-WS-120MS
- AKUN-009-CLOUDFLARE-VLESS-WS-131MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-78MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-73MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
