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
- AKUN-001-ORACLE-VLESS-WS-63MS
- AKUN-007-CLOUDWEBMANAGE-EU-FR-VLESS-WS-68MS
- AKUN-004-U1HOST-FRA-VLESS-WS-70MS
- AKUN-003-UNKNOWN-VLESS-WS-70MS
- AKUN-002-UNKNOWN-VLESS-WS-71MS
- AKUN-005-HOSTOFF-NET-VLESS-WS-75MS
- AKUN-006-UNKNOWN-VLESS-WS-78MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-78MS
- AKUN-009-CLOUDFLARE-VLESS-WS-111MS

## Streaming Pool
- AKUN-001-ORACLE-VLESS-WS-63MS
- AKUN-004-U1HOST-FRA-VLESS-WS-70MS
- AKUN-003-UNKNOWN-VLESS-WS-70MS
- AKUN-002-UNKNOWN-VLESS-WS-71MS
- AKUN-005-HOSTOFF-NET-VLESS-WS-75MS
- AKUN-008-CLOUDFLARE-VLESS-WS-78MS
- AKUN-006-UNKNOWN-VLESS-WS-78MS
- AKUN-009-CLOUDFLARE-VLESS-WS-111MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-CLOUDFLARE-VLESS-WS-81MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
