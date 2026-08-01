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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=219ms, nekobox=246ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-59MS` (url=220ms, nekobox=267ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=231ms, nekobox=271ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-71MS` (url=241ms, nekobox=251ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-62MS` (url=234ms, nekobox=269ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=224ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=276ms, nekobox=176ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS` (url=239ms, nekobox=176ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-80MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-89MS`
12. `AKUN-010-090227-VLESS-WS-113MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-80MS` (url=267ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-91MS` (url=241ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-150MS` (url=251ms, status=HTTP 204)
16. `AKUN-017-FASTVPSUS-IPV4-VLESS-WS-140MS` (url=346ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-165MS` (url=296ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-348MS` (url=776ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-442MS` (url=934ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-449MS` (url=984ms, status=HTTP 204)
21. `AKUN-023-SUKARIO-VLESS-WS-471MS` (url=714ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-513MS` (url=882ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-501MS` (url=1022ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-443MS` (url=783ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-487MS` (url=1185ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
