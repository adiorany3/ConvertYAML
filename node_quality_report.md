# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 4 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-GOV-VLESS-WS-112MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS
- AKUN-004-UNKNOWN-VLESS-WS-124MS
- AKUN-003-UNKNOWN-VLESS-WS-127MS
- AKUN-005-CLOUDFLARE-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS
- AKUN-006-GO-DADDY-COM-LLC-VLESS-WS-135MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-127MS
- AKUN-005-CLOUDFLARE-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS
- AKUN-010-CLOUDFLARE-VLESS-WS-135MS

## Streaming Pool
- AKUN-001-GOV-VLESS-WS-112MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS
- AKUN-004-UNKNOWN-VLESS-WS-124MS
- AKUN-003-UNKNOWN-VLESS-WS-127MS
- AKUN-008-CLOUDFLARE-VLESS-WS-127MS
- AKUN-005-CLOUDFLARE-VLESS-WS-133MS
- AKUN-007-CLOUDFLARE-VLESS-WS-133MS
- AKUN-010-CLOUDFLARE-VLESS-WS-135MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-103MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-SPEEDTEST-VLESS-WS-119MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-DEV-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-135MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
