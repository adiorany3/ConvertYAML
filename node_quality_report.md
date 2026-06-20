# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-001-CLOUDFLARE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-135MS
- AKUN-004-UNKNOWN-VLESS-WS-137MS
- AKUN-006-ADF-VLESS-WS-141MS
- AKUN-005-CLOUDFLARE-VLESS-WS-143MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS
- AKUN-007-MYBB-VLESS-WS-189MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-135MS
- AKUN-005-CLOUDFLARE-VLESS-WS-143MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-132MS
- AKUN-003-CLOUDFLARE-VLESS-WS-135MS
- AKUN-004-UNKNOWN-VLESS-WS-137MS
- AKUN-006-ADF-VLESS-WS-141MS
- AKUN-005-CLOUDFLARE-VLESS-WS-143MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS
- AKUN-008-MEDIUM-VLESS-WS-167MS
- AKUN-007-MYBB-VLESS-WS-189MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-006-CLOUDFLARE-VLESS-WS-137MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
