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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=223ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=220ms, nekobox=275ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=225ms, nekobox=267ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=233ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=232ms, nekobox=270ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=267ms, nekobox=264ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-64MS` (url=270ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-77MS` (url=284ms, nekobox=327ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-76MS` (url=295ms, nekobox=7177ms, status=no)
10. `AKUN-010-UNKNOWN-VLESS-WS-98MS` (url=478ms, nekobox=176ms, status=no)
11. `AKUN-009-UNKNOWN-VLESS-WS-100MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-107MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-131MS` (url=381ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-123MS` (url=312ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-115MS` (url=394ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=321ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-122MS` (url=285ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-134MS` (url=318ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-174MS` (url=299ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-105MS` (url=255ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-212MS` (url=296ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-257MS` (url=3944ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-259MS` (url=556ms, status=HTTP 204)
25. `AKUN-025-LT-LRTC-20060503-VLESS-WS-267MS` (url=554ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
