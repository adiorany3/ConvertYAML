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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=212ms, nekobox=245ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=214ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-75MS` (url=223ms, nekobox=254ms, status=yes)
4. `AKUN-004-GOOGLE-VLESS-WS-71MS` (url=209ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=208ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-74MS` (url=210ms, nekobox=240ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-71MS` (url=216ms, nekobox=243ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-76MS` (url=208ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS` (url=211ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=219ms, nekobox=248ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-120MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-107MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-111MS` (url=224ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-115MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-129MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-73MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-127MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-3666888-VLESS-WS-89MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-116MS` (url=235ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-98MS` (url=239ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-99MS` (url=244ms, status=HTTP 204)
23. `AKUN-023-ZOOM-VLESS-WS-85MS` (url=224ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-137MS` (url=266ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-234MS` (url=508ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
