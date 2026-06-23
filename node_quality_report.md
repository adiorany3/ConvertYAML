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
- AKUN-001-ORACLE-VLESS-WS-70MS
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-003-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-CLOUDFLARE-VLESS-WS-107MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS
- AKUN-007-CONFLU-VLESS-WS-228MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-003-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-CLOUDFLARE-VLESS-WS-107MS
- AKUN-008-CLOUDFLARE-VLESS-WS-256MS

## Streaming Pool
- AKUN-001-ORACLE-VLESS-WS-70MS
- AKUN-005-CLOUDFLARE-VLESS-WS-84MS
- AKUN-002-CLOUDFLARE-VLESS-WS-91MS
- AKUN-003-CLOUDFLARE-VLESS-WS-99MS
- AKUN-006-CLOUDFLARE-VLESS-WS-107MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS
- AKUN-007-CONFLU-VLESS-WS-228MS
- AKUN-008-CLOUDFLARE-VLESS-WS-256MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-002-CLOUDFLARE-VLESS-WS-74MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-DEV-VLESS-WS-77MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-009-CLOUDFLARE-VLESS-WS-94MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-CLOUDFLARE-VLESS-WS-92MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-113MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
