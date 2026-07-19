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
1. `AKUN-001-UNKNOWN-VLESS-WS-87MS` (url=204ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-88MS` (url=205ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-89MS` (url=197ms, nekobox=232ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-100MS` (url=213ms, nekobox=7173ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-97MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-97MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-103MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-89MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-113MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-RTCOMM-SRAVNI-RU-VLESS-WS-100MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-137MS` (url=256ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-ZVC-VLESS-WS-111MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=275ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-122MS` (url=264ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-99MS` (url=219ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-149MS` (url=250ms, status=HTTP 204)
24. `AKUN-024-NEXUSMODS-VLESS-WS-128MS` (url=225ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-133MS` (url=235ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
