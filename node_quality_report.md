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
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-67MS
- AKUN-001-CLOUDFLARE-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-LT-LRTC-20060503-VLESS-WS-74MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-005-ZVC-VLESS-WS-90MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-67MS
- AKUN-001-CLOUDFLARE-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS

## Streaming Pool
- AKUN-004-CLOUDFLARE-VLESS-WS-61MS
- AKUN-002-CLOUDFLARE-VLESS-WS-67MS
- AKUN-001-CLOUDFLARE-VLESS-WS-70MS
- AKUN-007-CLOUDFLARE-VLESS-WS-72MS
- AKUN-003-LT-LRTC-20060503-VLESS-WS-74MS
- AKUN-006-CLOUDFLARE-VLESS-WS-88MS
- AKUN-008-WPENG-VLESS-WS-88MS
- AKUN-005-ZVC-VLESS-WS-90MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-DEV-VLESS-WS-79MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-CLOUDFLARE-VLESS-WS-68MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
