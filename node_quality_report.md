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
- AKUN-001-UNKNOWN-VLESS-WS-135MS
- AKUN-005-CLOUDFLARE-VLESS-WS-150MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-159MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-167MS
- AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-176MS
- AKUN-007-CLOUDFLARE-VLESS-WS-178MS

## Tier 1B - WARM-UP-CF
- AKUN-008-CLOUDFLARE-VLESS-WS-140MS
- AKUN-005-CLOUDFLARE-VLESS-WS-150MS
- AKUN-010-CLOUDFLARE-VLESS-WS-166MS
- AKUN-007-CLOUDFLARE-VLESS-WS-178MS

## Streaming Pool
- AKUN-001-UNKNOWN-VLESS-WS-135MS
- AKUN-008-CLOUDFLARE-VLESS-WS-140MS
- AKUN-005-CLOUDFLARE-VLESS-WS-150MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-159MS
- AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS
- AKUN-010-CLOUDFLARE-VLESS-WS-166MS
- AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-167MS
- AKUN-007-CLOUDFLARE-VLESS-WS-178MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
