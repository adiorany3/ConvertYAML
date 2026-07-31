# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-003-UNKNOWN-VLESS-WS-63MS
- AKUN-005-ALIBABA-VLESS-WS-64MS
- AKUN-001-UNKNOWN-VLESS-WS-66MS
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-006-LEVIKOGJGFDD-VLESS-WS-69MS
- AKUN-002-MEDIUM-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS
- AKUN-008-CLOUDFLARE-VLESS-WS-93MS

## Streaming Pool
- AKUN-003-UNKNOWN-VLESS-WS-63MS
- AKUN-005-ALIBABA-VLESS-WS-64MS
- AKUN-001-UNKNOWN-VLESS-WS-66MS
- AKUN-004-CLOUDFLARE-VLESS-WS-68MS
- AKUN-006-LEVIKOGJGFDD-VLESS-WS-69MS
- AKUN-002-MEDIUM-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-90MS
- AKUN-008-CLOUDFLARE-VLESS-WS-93MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-SPEEDTEST-VLESS-WS-60MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-SPEEDTEST-VLESS-WS-62MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
