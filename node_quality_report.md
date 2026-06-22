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
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS
- AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-112MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-003-CLOUDFLARE-VLESS-WS-71MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-009-CLOUDFLARE-VLESS-WS-111MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-58MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS
- AKUN-003-CLOUDFLARE-VLESS-WS-71MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS
- AKUN-007-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS
- AKUN-009-CLOUDFLARE-VLESS-WS-111MS
- AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-112MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-CLOUDFLARE-VLESS-WS-80MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-83MS: ReadTimeout: HTTPSConnectionPool(host='www.gstatic.com', port=443): Read timed out. (read timeout=7.0)
- AKUN-010-CLOUDFLARE-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-76MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
