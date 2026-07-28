# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CL-65-49-192-0-19-VLESS-WS-81MS
- AKUN-004-UNKNOWN-VLESS-WS-91MS
- AKUN-005-UNKNOWN-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-006-UNKNOWN-VLESS-WS-103MS
- AKUN-007-UNKNOWN-VLESS-WS-116MS
- AKUN-003-UNKNOWN-VLESS-WS-130MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS

## Streaming Pool
- AKUN-001-CL-65-49-192-0-19-VLESS-WS-81MS
- AKUN-004-UNKNOWN-VLESS-WS-91MS
- AKUN-005-UNKNOWN-VLESS-WS-95MS
- AKUN-002-CLOUDFLARE-VLESS-WS-97MS
- AKUN-008-UNKNOWN-VLESS-WS-99MS
- AKUN-006-UNKNOWN-VLESS-WS-103MS
- AKUN-007-UNKNOWN-VLESS-WS-116MS
- AKUN-003-UNKNOWN-VLESS-WS-130MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-CLOUDFLARE-VLESS-WS-149MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
