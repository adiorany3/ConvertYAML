# Node Quality Report - Smart Stable

## Ringkasan
- Total proxy di YAML: 16
- WARM-UP harian: 7 node
- WARM-UP-CF Cloudflare/Worker: 2 node
- STREAMING-FAST: 8 node
- AUTO-FAST: 10 node
- FALLBACK: 16 referensi, manual backup: 6 node

## Rekomendasi Pakai
- Harian/browsing: pilih `WARM-UP` atau `AUTO-FAST`.
- Cloudflare/Worker dan streaming: pilih `WARM-UP-CF` atau `STREAMING-FAST`.
- Kalau koneksi putus-putus: pilih `FALLBACK`, karena urutannya sudah automatic strict dulu lalu manual backup.
- Router RAM kecil: pakai `openclash_lite.yaml`.

## Tier 1 - WARM-UP
- AKUN-003-UNKNOWN-VLESS-WS-136MS
- AKUN-007-ZVC-VLESS-WS-140MS
- AKUN-001-UNKNOWN-VLESS-WS-143MS
- AKUN-002-UNKNOWN-VLESS-WS-145MS
- AKUN-004-UNKNOWN-VLESS-WS-149MS
- AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-150MS
- AKUN-006-CLOUDFLARE-VLESS-WS-157MS

## Tier 1B - WARM-UP-CF
- AKUN-009-CLOUDFLARE-VLESS-WS-146MS
- AKUN-006-CLOUDFLARE-VLESS-WS-157MS

## Streaming Pool
- AKUN-003-UNKNOWN-VLESS-WS-136MS
- AKUN-007-ZVC-VLESS-WS-140MS
- AKUN-001-UNKNOWN-VLESS-WS-143MS
- AKUN-002-UNKNOWN-VLESS-WS-145MS
- AKUN-009-CLOUDFLARE-VLESS-WS-146MS
- AKUN-004-UNKNOWN-VLESS-WS-149MS
- AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-150MS
- AKUN-006-CLOUDFLARE-VLESS-WS-157MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
