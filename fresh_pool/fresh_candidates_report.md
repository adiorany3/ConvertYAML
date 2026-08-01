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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=206ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=233ms, nekobox=254ms, status=yes)
3. `AKUN-003-CCWU-VLESS-WS-79MS` (url=204ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=212ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-79MS` (url=204ms, nekobox=210ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-90MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-84MS`
10. `AKUN-009-008500-VLESS-WS-102MS`
11. `AKUN-010-DEV-VLESS-WS-86MS`
12. `AKUN-012-DEV-VLESS-WS-86MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-93MS` (url=220ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-100MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-89MS` (url=202ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-111MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-113MS` (url=228ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-137MS` (url=221ms, status=HTTP 204)
20. `AKUN-020-MYBB-VLESS-WS-122MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-120MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-92MS` (url=203ms, status=HTTP 204)
23. `AKUN-023-PAGES-VLESS-WS-122MS` (url=280ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-142MS` (url=213ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-122MS` (url=353ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
