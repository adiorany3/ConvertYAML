# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 14
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 3 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 14 referensi, manual backup: 4 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-005-CLOUDFLARE-VLESS-WS-52MS
- AKUN-003-UNKNOWN-VLESS-WS-53MS
- AKUN-001-CELESTARA-VLESS-WS-54MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-55MS
- AKUN-004-CLOUDFLARE-VLESS-WS-56MS
- AKUN-007-UNKNOWN-VLESS-WS-76MS
- AKUN-006-UNKNOWN-VLESS-WS-78MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-52MS
- AKUN-004-CLOUDFLARE-VLESS-WS-56MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS

## Streaming Pool
- AKUN-005-CLOUDFLARE-VLESS-WS-52MS
- AKUN-003-UNKNOWN-VLESS-WS-53MS
- AKUN-001-CELESTARA-VLESS-WS-54MS
- AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-55MS
- AKUN-004-CLOUDFLARE-VLESS-WS-56MS
- AKUN-007-UNKNOWN-VLESS-WS-76MS
- AKUN-006-UNKNOWN-VLESS-WS-78MS
- AKUN-010-CLOUDFLARE-VLESS-WS-96MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
