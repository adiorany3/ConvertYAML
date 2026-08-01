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
- AKUN-007-UNKNOWN-VLESS-WS-69MS
- AKUN-001-UNKNOWN-VLESS-WS-73MS
- AKUN-006-CLOUDFLARE-VLESS-WS-73MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-004-UNKNOWN-VLESS-WS-80MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-90MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-73MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-009-CLOUDFLARE-VLESS-WS-118MS
- AKUN-010-CLOUDFLARE-VLESS-WS-139MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-73MS
- AKUN-006-CLOUDFLARE-VLESS-WS-73MS
- AKUN-002-CLOUDFLARE-VLESS-WS-77MS
- AKUN-004-UNKNOWN-VLESS-WS-80MS
- AKUN-003-UNKNOWN-VLESS-WS-86MS
- AKUN-005-LEVIKOGJGFDD-VLESS-WS-90MS
- AKUN-009-CLOUDFLARE-VLESS-WS-118MS
- AKUN-010-CLOUDFLARE-VLESS-WS-139MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-79MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
