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
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS
- AKUN-001-UNKNOWN-VLESS-WS-80MS
- AKUN-003-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-COMPREND-NET-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-94MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-81MS
- AKUN-004-CLOUDFLARE-VLESS-WS-94MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS
- AKUN-008-CLOUDFLARE-VLESS-WS-116MS

## Streaming Pool
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS
- AKUN-001-UNKNOWN-VLESS-WS-80MS
- AKUN-003-CLOUDFLARE-VLESS-WS-81MS
- AKUN-006-COMPREND-NET-VLESS-WS-84MS
- AKUN-004-CLOUDFLARE-VLESS-WS-94MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS
- AKUN-005-CLOUDFLARE-VLESS-WS-107MS
- AKUN-008-CLOUDFLARE-VLESS-WS-116MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-86MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
