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
- AKUN-005-CLOUDFLARE-VLESS-WS-134MS
- AKUN-001-CLOUDFLARE-VLESS-WS-135MS
- AKUN-002-UNKNOWN-VLESS-WS-136MS
- AKUN-006-OPENAI-VLESS-WS-137MS
- AKUN-003-CLOUDFLARE-VLESS-WS-137MS
- AKUN-004-UNKNOWN-VLESS-WS-139MS
- AKUN-007-CLOUDFLARE-VLESS-WS-156MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-134MS
- AKUN-001-CLOUDFLARE-VLESS-WS-135MS
- AKUN-003-CLOUDFLARE-VLESS-WS-137MS
- AKUN-007-CLOUDFLARE-VLESS-WS-156MS

## Streaming Pool
- AKUN-005-CLOUDFLARE-VLESS-WS-134MS
- AKUN-001-CLOUDFLARE-VLESS-WS-135MS
- AKUN-002-UNKNOWN-VLESS-WS-136MS
- AKUN-006-OPENAI-VLESS-WS-137MS
- AKUN-003-CLOUDFLARE-VLESS-WS-137MS
- AKUN-004-UNKNOWN-VLESS-WS-139MS
- AKUN-008-UNKNOWN-VLESS-WS-148MS
- AKUN-007-CLOUDFLARE-VLESS-WS-156MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-007-DEV-VLESS-WS-135MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
