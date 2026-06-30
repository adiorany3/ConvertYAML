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
- AKUN-003-CLOUDFLARE-VLESS-WS-92MS
- AKUN-001-ZVC-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-96MS
- AKUN-002-CLOUDFLARE-VLESS-WS-96MS
- AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-98MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-005-COMPREND-NET-VLESS-WS-110MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-92MS
- AKUN-006-CLOUDFLARE-VLESS-WS-96MS
- AKUN-002-CLOUDFLARE-VLESS-WS-96MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-010-CLOUDFLARE-VLESS-WS-124MS

## Streaming Pool
- AKUN-003-CLOUDFLARE-VLESS-WS-92MS
- AKUN-001-ZVC-VLESS-WS-95MS
- AKUN-006-CLOUDFLARE-VLESS-WS-96MS
- AKUN-002-CLOUDFLARE-VLESS-WS-96MS
- AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-98MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-005-COMPREND-NET-VLESS-WS-110MS
- AKUN-010-CLOUDFLARE-VLESS-WS-124MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-CLOUDFLARE-VLESS-WS-115MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-132MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
