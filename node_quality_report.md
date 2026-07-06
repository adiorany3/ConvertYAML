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
- AKUN-007-CLOUDFLARE-VLESS-WS-131MS
- AKUN-003-090227-VLESS-WS-137MS
- AKUN-004-UNKNOWN-VLESS-WS-142MS
- AKUN-001-UNKNOWN-VLESS-WS-142MS
- AKUN-002-UNKNOWN-VLESS-WS-148MS
- AKUN-005-WEBEX-VLESS-WS-152MS
- AKUN-006-CLOUDFLARE-VLESS-WS-159MS

## Tier 1B - WARM-UP-CF
- AKUN-007-CLOUDFLARE-VLESS-WS-131MS
- AKUN-008-CLOUDFLARE-VLESS-WS-150MS
- AKUN-006-CLOUDFLARE-VLESS-WS-159MS

## Streaming Pool
- AKUN-007-CLOUDFLARE-VLESS-WS-131MS
- AKUN-003-090227-VLESS-WS-137MS
- AKUN-004-UNKNOWN-VLESS-WS-142MS
- AKUN-001-UNKNOWN-VLESS-WS-142MS
- AKUN-002-UNKNOWN-VLESS-WS-148MS
- AKUN-008-CLOUDFLARE-VLESS-WS-150MS
- AKUN-005-WEBEX-VLESS-WS-152MS
- AKUN-006-CLOUDFLARE-VLESS-WS-159MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
