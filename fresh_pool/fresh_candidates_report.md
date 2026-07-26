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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=315ms, nekobox=299ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=313ms, nekobox=335ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=314ms, nekobox=306ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=299ms, nekobox=363ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=275ms, nekobox=312ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-78MS` (url=271ms, nekobox=385ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=290ms, nekobox=318ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-74MS` (url=305ms, nekobox=298ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-91MS` (url=347ms, nekobox=389ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=272ms, nekobox=309ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-78MS` (url=326ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-87MS` (url=317ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=278ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-113MS` (url=349ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-93MS` (url=275ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-111MS` (url=280ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=323ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-124MS` (url=359ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-117MS` (url=276ms, status=HTTP 204)
20. `AKUN-020-CCWU-VLESS-WS-97MS` (url=325ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-115MS` (url=283ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-161MS` (url=442ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-126MS` (url=334ms, status=HTTP 204)
24. `AKUN-024-ZVC-VLESS-WS-75MS` (url=276ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-303MS` (url=2434ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
