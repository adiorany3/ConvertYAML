# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 1 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-64MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS
- AKUN-006-UNKNOWN-VLESS-WS-71MS
- AKUN-005-UNKNOWN-VLESS-WS-92MS
- AKUN-003-UNKNOWN-VLESS-WS-107MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS
- AKUN-007-UNKNOWN-VLESS-WS-141MS

## Tier 1B - WARM-UP-CF
- AKUN-010-CLOUDFLARE-VLESS-WS-282MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-64MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS
- AKUN-006-UNKNOWN-VLESS-WS-71MS
- AKUN-005-UNKNOWN-VLESS-WS-92MS
- AKUN-003-UNKNOWN-VLESS-WS-107MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS
- AKUN-007-UNKNOWN-VLESS-WS-141MS
- AKUN-010-CLOUDFLARE-VLESS-WS-282MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-003-DEV-VLESS-WS-104MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-SPEEDTEST-VLESS-WS-89MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-154MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-141MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-92MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-DEV-VLESS-WS-112MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
