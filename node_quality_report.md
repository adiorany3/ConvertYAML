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
- AKUN-001-ORACLE-VLESS-WS-124MS
- AKUN-006-UNKNOWN-VLESS-WS-136MS
- AKUN-005-CLOUDFLARE-VLESS-WS-141MS
- AKUN-007-DIGITALOCEAN-VLESS-WS-141MS
- AKUN-002-CLOUDFLARE-VLESS-WS-144MS
- AKUN-003-HOSTOFF-NET-VLESS-WS-145MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-148MS

## Tier 1B - WARM-UP-CF
- AKUN-005-CLOUDFLARE-VLESS-WS-141MS
- AKUN-002-CLOUDFLARE-VLESS-WS-144MS
- AKUN-008-CLOUDFLARE-VLESS-WS-145MS
- AKUN-009-CLOUDFLARE-VLESS-WS-160MS

## Streaming Pool
- AKUN-001-ORACLE-VLESS-WS-124MS
- AKUN-006-UNKNOWN-VLESS-WS-136MS
- AKUN-005-CLOUDFLARE-VLESS-WS-141MS
- AKUN-002-CLOUDFLARE-VLESS-WS-144MS
- AKUN-003-HOSTOFF-NET-VLESS-WS-145MS
- AKUN-008-CLOUDFLARE-VLESS-WS-145MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-148MS
- AKUN-009-CLOUDFLARE-VLESS-WS-160MS

## Node Berisiko dari NekoBox/sing-box Test
- Tidak ada yang gagal pada laporan terakhir

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
