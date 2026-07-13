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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=223ms, nekobox=253ms, status=yes)
2. `AKUN-002-DEV-VLESS-WS-71MS` (url=230ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-67MS` (url=223ms, nekobox=259ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=250ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=243ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=221ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=233ms, nekobox=255ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-76MS` (url=248ms, nekobox=252ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-91MS` (url=219ms, nekobox=254ms, status=yes)
10. `AKUN-010-ES-FORNEX-20160629-VLESS-WS-88MS` (url=225ms, nekobox=260ms, status=yes)
11. `AKUN-011-SHOPIFY-VLESS-WS-80MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-70MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-99MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-1PASSWORD-VLESS-WS-95MS` (url=235ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-79MS` (url=241ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=249ms, status=HTTP 204)
18. `AKUN-018-UDACITY-VLESS-WS-127MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-MYBB-VLESS-WS-129MS` (url=231ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-106MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-95MS` (url=275ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-143MS` (url=218ms, status=HTTP 204)
23. `AKUN-023-PUBLICDOMAINREGISTRY-NET-VLESS-WS-118MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-ZOOM-VLESS-WS-129MS` (url=233ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-350MS` (url=770ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
