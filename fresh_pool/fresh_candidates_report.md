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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=215ms, nekobox=248ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-64MS` (url=217ms, nekobox=252ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-67MS` (url=295ms, nekobox=241ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=217ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS` (url=220ms, nekobox=252ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-68MS` (url=458ms, nekobox=246ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-70MS` (url=223ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, nekobox=253ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-65MS` (url=239ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS` (url=219ms, nekobox=244ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=1186ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-NODEHOST-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=413ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-73MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-114MS` (url=196ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-71MS` (url=219ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-359MS` (url=795ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-373MS` (url=1857ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-365MS` (url=866ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-387MS` (url=784ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-364MS` (url=728ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-389MS` (url=840ms, status=HTTP 204)
24. `AKUN-028-QZZ-VLESS-WS-575MS` (url=1045ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-703MS` (url=1146ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
