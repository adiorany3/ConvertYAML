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
- AKUN-001-090227-VLESS-WS-66MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-108MS
- AKUN-005-CLOUDFLARE-VLESS-WS-113MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS

## Tier 1B - WARM-UP-CF
- AKUN-006-CLOUDFLARE-VLESS-WS-108MS
- AKUN-005-CLOUDFLARE-VLESS-WS-113MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS
- AKUN-009-CLOUDFLARE-VLESS-WS-230MS

## Streaming Pool
- AKUN-001-090227-VLESS-WS-66MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS
- AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS
- AKUN-006-CLOUDFLARE-VLESS-WS-108MS
- AKUN-005-CLOUDFLARE-VLESS-WS-113MS
- AKUN-007-CLOUDFLARE-VLESS-WS-122MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS
- AKUN-009-CLOUDFLARE-VLESS-WS-230MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-UNKNOWN-VLESS-WS-78MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-005-CLOUDFLARE-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-DEV-VLESS-WS-137MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-CLOUDFLARE-VLESS-WS-133MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-94MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-97MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-89MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
