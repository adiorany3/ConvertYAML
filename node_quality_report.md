# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 18
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 5 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 18 referensi, manual backup: 8 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-73MS
- AKUN-004-CLOUDFLARE-VLESS-WS-74MS
- AKUN-001-ORACLE-VLESS-WS-77MS
- AKUN-006-FMN5-RENTED-NET2-VLESS-WS-94MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-102MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-74MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-102MS
- AKUN-008-CLOUDFLARE-VLESS-WS-106MS
- AKUN-009-CLOUDFLARE-VLESS-WS-135MS

## Streaming Pool
- AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-73MS
- AKUN-004-CLOUDFLARE-VLESS-WS-74MS
- AKUN-001-ORACLE-VLESS-WS-77MS
- AKUN-006-FMN5-RENTED-NET2-VLESS-WS-94MS
- AKUN-003-CLOUDFLARE-VLESS-WS-96MS
- AKUN-005-CLOUDFLARE-VLESS-WS-102MS
- AKUN-008-CLOUDFLARE-VLESS-WS-106MS
- AKUN-009-CLOUDFLARE-VLESS-WS-135MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-82MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
