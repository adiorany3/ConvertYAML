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
- AKUN-002-UNKNOWN-VLESS-WS-128MS
- AKUN-001-UNKNOWN-VLESS-WS-133MS
- AKUN-004-CLOUDFLARE-VLESS-WS-134MS
- AKUN-005-CLOUDFLARE-VLESS-WS-135MS
- AKUN-006-CLOUDFLARE-VLESS-WS-135MS
- AKUN-003-UNKNOWN-VLESS-WS-136MS
- AKUN-007-CLOUDFLARE-VLESS-WS-149MS

## Tier 1B - WARM-UP-CF
- AKUN-004-CLOUDFLARE-VLESS-WS-134MS
- AKUN-005-CLOUDFLARE-VLESS-WS-135MS
- AKUN-006-CLOUDFLARE-VLESS-WS-135MS
- AKUN-007-CLOUDFLARE-VLESS-WS-149MS
- AKUN-010-CLOUDFLARE-VLESS-WS-191MS

## Streaming Pool
- AKUN-002-UNKNOWN-VLESS-WS-128MS
- AKUN-001-UNKNOWN-VLESS-WS-133MS
- AKUN-004-CLOUDFLARE-VLESS-WS-134MS
- AKUN-005-CLOUDFLARE-VLESS-WS-135MS
- AKUN-006-CLOUDFLARE-VLESS-WS-135MS
- AKUN-003-UNKNOWN-VLESS-WS-136MS
- AKUN-007-CLOUDFLARE-VLESS-WS-149MS
- AKUN-010-CLOUDFLARE-VLESS-WS-191MS

## Node Berisiko dari NekoBox/sing-box Test
- AKUN-001-CLOUDFLARE-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-002-DEV-VLESS-WS-128MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-003-CLOUDFLARE-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-006-DEV-VLESS-WS-132MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-007-DEV-VLESS-WS-134MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-008-DEV-VLESS-WS-131MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-011-DEV-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-012-UNKNOWN-VLESS-WS-131MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-013-CLOUDFLARE-VLESS-WS-139MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-017-CLOUDFLARE-VLESS-WS-135MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-019-DEV-VLESS-WS-130MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
- AKUN-021-UNKNOWN-VLESS-WS-141MS: ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

## Catatan Smart Mode
- Health-check cepat hanya untuk pool kecil, bukan semua node.
- Cloudflare/Worker punya endpoint test sendiri: `https://cp.cloudflare.com`.
- `fake-ip-filter` diperluas untuk domain LAN, NTP, connectivity check, router, dan perbankan.
