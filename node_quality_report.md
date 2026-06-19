# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-CLOUDFLARE-VLESS-WS-100MS
- AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-101MS
- AKUN-005-MYBB-VLESS-WS-120MS
- AKUN-003-UNKNOWN-VLESS-WS-123MS
- AKUN-004-UNKNOWN-VLESS-WS-128MS
- AKUN-006-CLOUDFLARE-VLESS-WS-132MS
- AKUN-007-UNKNOWN-VLESS-WS-132MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-100MS
- AKUN-006-CLOUDFLARE-VLESS-WS-132MS

## Streaming Pool
- AKUN-002-CLOUDFLARE-VLESS-WS-100MS
- AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-101MS
- AKUN-005-MYBB-VLESS-WS-120MS
- AKUN-003-UNKNOWN-VLESS-WS-123MS
- AKUN-004-UNKNOWN-VLESS-WS-128MS
- AKUN-006-CLOUDFLARE-VLESS-WS-132MS
- AKUN-007-UNKNOWN-VLESS-WS-132MS
- AKUN-008-UNKNOWN-VLESS-WS-135MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-102MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-002-CLOUDFLARE-VLESS-WS-109MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-119MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-124MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
