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
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-003-CLOUDFLARE-VLESS-WS-131MS
- AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-137MS
- AKUN-007-UNKNOWN-VLESS-WS-142MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS
- AKUN-004-CLOUDFLARE-VLESS-WS-146MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-003-CLOUDFLARE-VLESS-WS-131MS
- AKUN-004-CLOUDFLARE-VLESS-WS-146MS
- AKUN-009-CLOUDFLARE-VLESS-WS-163MS

## Streaming Pool
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS
- AKUN-001-CLOUDFLARE-VLESS-WS-113MS
- AKUN-003-CLOUDFLARE-VLESS-WS-131MS
- AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-137MS
- AKUN-007-UNKNOWN-VLESS-WS-142MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-143MS
- AKUN-004-CLOUDFLARE-VLESS-WS-146MS
- AKUN-009-CLOUDFLARE-VLESS-WS-163MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-010-CLOUDFLARE-VLESS-WS-132MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-160MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-122MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
