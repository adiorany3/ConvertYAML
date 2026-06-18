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
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS
- AKUN-001-CNAE-VLESS-WS-104MS
- AKUN-006-CLOUDFLARE-VLESS-WS-119MS
- AKUN-004-UNKNOWN-VLESS-WS-121MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-005-OPENAI-VLESS-WS-125MS
- AKUN-007-CLOUDFLARE-VLESS-WS-129MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-118MS
- AKUN-006-CLOUDFLARE-VLESS-WS-119MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-007-CLOUDFLARE-VLESS-WS-129MS
- AKUN-010-CLOUDFLARE-VLESS-WS-285MS

## Streaming Pool
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS
- AKUN-001-CNAE-VLESS-WS-104MS
- AKUN-008-CLOUDFLARE-VLESS-WS-118MS
- AKUN-006-CLOUDFLARE-VLESS-WS-119MS
- AKUN-004-UNKNOWN-VLESS-WS-121MS
- AKUN-003-CLOUDFLARE-VLESS-WS-122MS
- AKUN-007-CLOUDFLARE-VLESS-WS-129MS
- AKUN-010-CLOUDFLARE-VLESS-WS-285MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-93MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-DEV-VLESS-WS-120MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-138MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-297MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
