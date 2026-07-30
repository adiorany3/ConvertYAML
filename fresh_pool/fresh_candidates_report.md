# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-99MS` (url=276ms, nekobox=833ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=805ms, nekobox=821ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS` (url=269ms, nekobox=816ms, status=yes)
4. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-91MS` (url=1493ms, nekobox=2094ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-104MS` (url=258ms, nekobox=828ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-113MS` (url=257ms, nekobox=522ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-193MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-91MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-138MS` (url=789ms, status=HTTP 204)
13. `AKUN-013-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-97MS` (url=299ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=777ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-113MS` (url=280ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-123MS` (url=655ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=283ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-109MS` (url=275ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-114MS` (url=790ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-103MS` (url=302ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-269MS` (url=275ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-400MS` (url=235ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-543MS` (url=799ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-108MS` (url=802ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-165MS` (url=863ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
