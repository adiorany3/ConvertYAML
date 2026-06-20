# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 12
- WARM-UP harian: 6 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 6 node
- AUTO-FAST: 6 node
- FALLBACK: 12 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-UNKNOWN-VLESS-WS-67MS
- AKUN-002-CLOUDFLARE-VLESS-WS-334MS
- AKUN-005-CLOUDFLARE-VLESS-WS-353MS
- AKUN-003-CLOUDFLARE-VLESS-WS-373MS
- AKUN-004-CLOUDFLARE-VLESS-WS-388MS
- AKUN-006-CLOUDFLARE-VLESS-WS-434MS

## Tier 1B - WARM-UP-CF
- AKUN-002-CLOUDFLARE-VLESS-WS-334MS
- AKUN-005-CLOUDFLARE-VLESS-WS-353MS
- AKUN-003-CLOUDFLARE-VLESS-WS-373MS
- AKUN-004-CLOUDFLARE-VLESS-WS-388MS
- AKUN-006-CLOUDFLARE-VLESS-WS-434MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-67MS
- AKUN-002-CLOUDFLARE-VLESS-WS-334MS
- AKUN-005-CLOUDFLARE-VLESS-WS-353MS
- AKUN-003-CLOUDFLARE-VLESS-WS-373MS
- AKUN-004-CLOUDFLARE-VLESS-WS-388MS
- AKUN-006-CLOUDFLARE-VLESS-WS-434MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-89MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-004-SPEEDTEST-VLESS-WS-119MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-016-UNKNOWN-VLESS-WS-640MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-023-UNKNOWN-VLESS-WS-625MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-026-UNKNOWN-VLESS-WS-611MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-027-UNKNOWN-VLESS-WS-619MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-028-UNKNOWN-VLESS-WS-663MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
