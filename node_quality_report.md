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
- AKUN-001-CLOUDFLARE-VLESS-WS-131MS
- AKUN-003-UNKNOWN-VLESS-WS-146MS
- AKUN-002-CLOUDFLARE-VLESS-WS-150MS
- AKUN-006-466688-VLESS-WS-153MS
- AKUN-007-ALIBABA-VLESS-WS-153MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-159MS
- AKUN-005-UNKNOWN-VLESS-WS-170MS

## Tier 1B - WARM-UP-CF
- AKUN-001-CLOUDFLARE-VLESS-WS-131MS
- AKUN-002-CLOUDFLARE-VLESS-WS-150MS

## Streaming Pool
- AKUN-001-CLOUDFLARE-VLESS-WS-131MS
- AKUN-003-UNKNOWN-VLESS-WS-146MS
- AKUN-002-CLOUDFLARE-VLESS-WS-150MS
- AKUN-006-466688-VLESS-WS-153MS
- AKUN-007-ALIBABA-VLESS-WS-153MS
- AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-159MS
- AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-161MS
- AKUN-005-UNKNOWN-VLESS-WS-170MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-135MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-142MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-DEV-VLESS-WS-155MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-148MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-UNKNOWN-VLESS-WS-151MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-CLOUDFLARE-VLESS-WS-164MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-014-CLOUDFLARE-VLESS-WS-141MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-015-CLOUDFLARE-VLESS-WS-171MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
