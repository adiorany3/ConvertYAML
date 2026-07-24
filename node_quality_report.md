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
- AKUN-002-CLOUDFLARE-VLESS-WS-82MS
- AKUN-003-UNKNOWN-VLESS-WS-84MS
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS
- AKUN-006-UNKNOWN-VLESS-WS-117MS
- AKUN-007-UNKNOWN-VLESS-WS-138MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-82MS
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS

## Streaming Pool
- AKUN-002-CLOUDFLARE-VLESS-WS-82MS
- AKUN-003-UNKNOWN-VLESS-WS-84MS
- AKUN-001-CLOUDFLARE-VLESS-WS-85MS
- AKUN-005-CLOUDFLARE-VLESS-WS-92MS
- AKUN-004-CLOUDFLARE-VLESS-WS-103MS
- AKUN-006-UNKNOWN-VLESS-WS-117MS
- AKUN-008-LEVIKOGJGFDD-VLESS-WS-131MS
- AKUN-007-UNKNOWN-VLESS-WS-138MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-SPEEDTEST-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-SPEEDTEST-VLESS-WS-127MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
