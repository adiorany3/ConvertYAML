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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-94MS` (url=234ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-97MS` (url=332ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=212ms, nekobox=295ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=230ms, nekobox=271ms, status=yes)
5. `AKUN-005-SHOPIFY-VLESS-WS-107MS` (url=252ms, nekobox=270ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-117MS` (url=217ms, nekobox=244ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-118MS` (url=248ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-113MS` (url=251ms, nekobox=7177ms, status=no)
9. `AKUN-008-UNKNOWN-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS`
11. `AKUN-010-HETZNER-VLESS-WS-120MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-118MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-122MS` (url=260ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-139MS` (url=280ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-147MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-148MS` (url=254ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-158MS` (url=564ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-131MS` (url=264ms, status=HTTP 204)
20. `AKUN-020-ES-FORNEX-20160629-VLESS-WS-100MS` (url=224ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-106MS` (url=257ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-96MS` (url=254ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-268MS` (url=398ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-197MS` (url=264ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-213MS` (url=244ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
