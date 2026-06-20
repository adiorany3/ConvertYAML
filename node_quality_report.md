# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 13
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 7 node
- AUTO-FAST: 7 node
- FALLBACK: 13 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-381MS
- AKUN-004-UNKNOWN-VLESS-WS-387MS
- AKUN-003-CLOUDFLARE-VLESS-WS-400MS
- AKUN-002-CLOUDFLARE-VLESS-WS-416MS
- AKUN-005-CLOUDFLARE-VLESS-WS-549MS
- AKUN-006-UNKNOWN-VLESS-WS-809MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-381MS
- AKUN-003-CLOUDFLARE-VLESS-WS-400MS
- AKUN-002-CLOUDFLARE-VLESS-WS-416MS
- AKUN-005-CLOUDFLARE-VLESS-WS-549MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-117MS
- AKUN-007-CLOUDFLARE-VLESS-WS-381MS
- AKUN-004-UNKNOWN-VLESS-WS-387MS
- AKUN-003-CLOUDFLARE-VLESS-WS-400MS
- AKUN-002-CLOUDFLARE-VLESS-WS-416MS
- AKUN-005-CLOUDFLARE-VLESS-WS-549MS
- AKUN-006-UNKNOWN-VLESS-WS-809MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-112MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-CLOUDFLARE-VLESS-WS-194MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-647MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-637MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-CLOUDFLARE-VLESS-WS-649MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-018-CLOUDFLARE-VLESS-WS-645MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-019-CLOUDFLARE-VLESS-WS-648MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-021-CLOUDFLARE-VLESS-WS-638MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-022-CLOUDFLARE-VLESS-WS-646MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-023-CLOUDFLARE-VLESS-WS-647MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-024-CLOUDFLARE-VLESS-WS-659MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-025-CLOUDFLARE-VLESS-WS-750MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-027-CLOUDFLARE-VLESS-WS-765MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-028-UNKNOWN-VLESS-WS-750MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
