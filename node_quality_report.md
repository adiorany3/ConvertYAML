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
- AKUN-002-UNKNOWN-VLESS-WS-110MS
- AKUN-003-DIGITALOCEAN-VLESS-WS-123MS
- AKUN-001-CLOUDFLARE-VLESS-WS-128MS
- AKUN-004-UNKNOWN-VLESS-WS-129MS
- AKUN-005-008500-VLESS-WS-132MS
- AKUN-006-UNKNOWN-VLESS-WS-133MS
- AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-139MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-128MS
- AKUN-010-CLOUDFLARE-VLESS-WS-133MS
- AKUN-008-CLOUDFLARE-VLESS-WS-152MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-110MS
- AKUN-003-DIGITALOCEAN-VLESS-WS-123MS
- AKUN-001-CLOUDFLARE-VLESS-WS-128MS
- AKUN-004-UNKNOWN-VLESS-WS-129MS
- AKUN-005-008500-VLESS-WS-132MS
- AKUN-006-UNKNOWN-VLESS-WS-133MS
- AKUN-010-CLOUDFLARE-VLESS-WS-133MS
- AKUN-008-CLOUDFLARE-VLESS-WS-152MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-005-CLOUDFLARE-VLESS-WS-117MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
