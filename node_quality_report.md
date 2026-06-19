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
- AKUN-002-UNKNOWN-VLESS-WS-76MS
- AKUN-004-UNKNOWN-VLESS-WS-77MS
- AKUN-003-008500-VLESS-WS-78MS
- AKUN-001-UNKNOWN-VLESS-WS-82MS
- AKUN-007-UNKNOWN-VLESS-WS-82MS
- AKUN-006-CLOUDFLARE-VLESS-WS-99MS
- AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-97MS
- AKUN-006-CLOUDFLARE-VLESS-WS-99MS
- AKUN-009-CLOUDFLARE-VLESS-WS-123MS
- AKUN-010-CLOUDFLARE-VLESS-WS-270MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-76MS
- AKUN-004-UNKNOWN-VLESS-WS-77MS
- AKUN-003-008500-VLESS-WS-78MS
- AKUN-001-UNKNOWN-VLESS-WS-82MS
- AKUN-008-CLOUDFLARE-VLESS-WS-97MS
- AKUN-006-CLOUDFLARE-VLESS-WS-99MS
- AKUN-009-CLOUDFLARE-VLESS-WS-123MS
- AKUN-010-CLOUDFLARE-VLESS-WS-270MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-DEV-VLESS-WS-95MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-010-DEV-VLESS-WS-84MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-DEV-VLESS-WS-104MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
