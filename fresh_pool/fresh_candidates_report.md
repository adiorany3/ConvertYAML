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
1. `AKUN-001-UNKNOWN-VLESS-WS-88MS` (url=212ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-91MS` (url=221ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=214ms, nekobox=260ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-96MS` (url=202ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=219ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=214ms, nekobox=238ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-94MS` (url=233ms, nekobox=249ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS` (url=229ms, nekobox=287ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=211ms, nekobox=268ms, status=yes)
10. `AKUN-010-DIXONS-VLESS-WS-100MS` (url=213ms, nekobox=254ms, status=yes)
11. `AKUN-011-UK-GB-DCL-01-20191003-VLESS-WS-96MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-90MS` (url=281ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-124MS` (url=271ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-144MS` (url=256ms, status=HTTP 204)
17. `AKUN-017-POLICE-VLESS-WS-163MS` (url=303ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-384MS` (url=2442ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-390MS` (url=816ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-435MS` (url=2135ms, status=HTTP 204)
21. `AKUN-022-IRCYBERSEC-VLESS-WS-448MS` (url=1011ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-689MS` (url=1100ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-694MS` (url=1159ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-721MS` (url=1166ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-741MS` (url=1230ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
