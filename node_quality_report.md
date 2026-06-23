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
- AKUN-001-UNKNOWN-VLESS-WS-100MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS
- AKUN-003-CLOUDFLARE-VLESS-WS-126MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS
- AKUN-004-UNKNOWN-VLESS-WS-143MS
- AKUN-005-CLOUDFLARE-VLESS-WS-155MS
- AKUN-006-UNKNOWN-VLESS-WS-165MS

## Tier 1B - WARM-UP-CF
- AKUN-003-CLOUDFLARE-VLESS-WS-126MS
- AKUN-009-CLOUDFLARE-VLESS-WS-134MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS
- AKUN-005-CLOUDFLARE-VLESS-WS-155MS
- AKUN-008-CLOUDFLARE-VLESS-WS-162MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-100MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-116MS
- AKUN-003-CLOUDFLARE-VLESS-WS-126MS
- AKUN-009-CLOUDFLARE-VLESS-WS-134MS
- AKUN-007-CLOUDFLARE-VLESS-WS-140MS
- AKUN-004-UNKNOWN-VLESS-WS-143MS
- AKUN-005-CLOUDFLARE-VLESS-WS-155MS
- AKUN-008-CLOUDFLARE-VLESS-WS-162MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-004-CLOUDFLARE-VLESS-WS-127MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-CLOUDFLARE-VLESS-WS-124MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-167MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-154MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
