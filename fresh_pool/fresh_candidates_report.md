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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-90MS` (url=215ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-84MS` (url=207ms, nekobox=254ms, status=yes)
3. `AKUN-003-PAGES-VLESS-WS-89MS` (url=229ms, nekobox=261ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=231ms, nekobox=250ms, status=yes)
5. `AKUN-005-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=312ms, nekobox=389ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-96MS` (url=204ms, nekobox=261ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-103MS` (url=261ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=217ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-129MS` (url=218ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-127MS` (url=223ms, nekobox=316ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-150MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-89MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-117MS` (url=246ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-170MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-126MS` (url=245ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-98MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-186MS` (url=225ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-242MS` (url=518ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-252MS` (url=549ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-279MS` (url=617ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-296MS` (url=583ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-290MS` (url=592ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-288MS` (url=612ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
