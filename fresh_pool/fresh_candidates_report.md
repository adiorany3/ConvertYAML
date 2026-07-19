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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-97MS` (url=308ms, nekobox=351ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-99MS` (url=318ms, nekobox=338ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-120MS` (url=280ms, nekobox=321ms, status=yes)
4. `AKUN-004-BGP48-HK-VLESS-WS-128MS` (url=333ms, nekobox=352ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-131MS` (url=259ms, nekobox=222ms, status=no)
6. `AKUN-005-DEV-VLESS-WS-123MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-136MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-137MS`
9. `AKUN-008-466688-VLESS-WS-100MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-148MS`
12. `AKUN-012-GLOBAL-COMMUNICATIONS-VLESS-WS-115MS` (url=315ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-153MS` (url=393ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-109MS` (url=339ms, status=HTTP 204)
15. `AKUN-015-DIXONS-VLESS-WS-152MS` (url=290ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=547ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-115MS` (url=313ms, status=HTTP 204)
18. `AKUN-018-DIXONS-VLESS-WS-170MS` (url=302ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-174MS` (url=253ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-184MS` (url=527ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-313MS` (url=645ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-331MS` (url=676ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-317MS` (url=605ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-112MS` (url=307ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-321MS` (url=671ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
