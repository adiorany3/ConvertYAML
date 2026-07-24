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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=213ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=212ms, nekobox=308ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=220ms, nekobox=243ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=227ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=205ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, nekobox=254ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS` (url=235ms, nekobox=244ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-99MS` (url=225ms, nekobox=247ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-109MS` (url=227ms, nekobox=294ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS` (url=212ms, nekobox=262ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-123MS` (url=257ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-127MS` (url=254ms, status=HTTP 204)
14. `AKUN-014-DEV-VLESS-WS-112MS` (url=254ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-100MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=268ms, status=HTTP 204)
17. `AKUN-017-SHOPIFY-VLESS-WS-148MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-122MS` (url=249ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-90MS` (url=272ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-134MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-163MS` (url=288ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-158MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CF-BYOIP-188-164-248-0-2-VLESS-WS-169MS` (url=327ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-126MS` (url=250ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-128MS` (url=312ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
