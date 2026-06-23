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
- AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS
- AKUN-003-CLOUDFLARE-VLESS-WS-64MS
- AKUN-005-CLOUDFLARE-VLESS-WS-68MS
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS
- AKUN-006-BROADNNET-KR-VLESS-WS-82MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS
- AKUN-007-KIRINO-31-25-88-0-24-VLESS-WS-93MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-64MS
- AKUN-005-CLOUDFLARE-VLESS-WS-68MS
- AKUN-009-CLOUDFLARE-VLESS-WS-367MS
- AKUN-010-CLOUDFLARE-VLESS-WS-372MS

## Streaming Pool
- AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS
- AKUN-008-CLOUDFLARE-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-64MS
- AKUN-005-CLOUDFLARE-VLESS-WS-68MS
- AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS
- AKUN-009-CLOUDFLARE-VLESS-WS-367MS
- AKUN-010-CLOUDFLARE-VLESS-WS-372MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-009-DIGITALOCEAN-VLESS-WS-116MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
