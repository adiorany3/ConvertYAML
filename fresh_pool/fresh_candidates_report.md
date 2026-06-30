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
1. `AKUN-001-ZVC-VLESS-WS-95MS` (url=220ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-96MS` (url=230ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=236ms, nekobox=3644ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-98MS` (url=231ms, nekobox=251ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-110MS` (url=252ms, nekobox=309ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-96MS` (url=239ms, nekobox=241ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS` (url=233ms, nekobox=275ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-98MS` (url=220ms, nekobox=271ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS` (url=223ms, nekobox=221ms, status=no)
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-107MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=247ms, nekobox=251ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-124MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-121MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-135MS` (url=285ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-98MS` (url=289ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-125MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-158MS` (url=254ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-137MS` (url=346ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-169MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-118MS` (url=229ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-122MS` (url=258ms, status=HTTP 204)
23. `AKUN-023-BIGCOMMERCE-VLESS-WS-137MS` (url=242ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-171MS` (url=235ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-378MS` (url=809ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
