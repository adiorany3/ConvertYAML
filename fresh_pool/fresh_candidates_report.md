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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=204ms, nekobox=227ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=231ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-94MS` (url=203ms, nekobox=267ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=232ms, nekobox=256ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-91MS` (url=281ms, nekobox=246ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=202ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS` (url=211ms, nekobox=237ms, status=yes)
8. `AKUN-008-1PASSWORD-VLESS-WS-100MS` (url=234ms, nekobox=309ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS` (url=246ms, nekobox=248ms, status=yes)
10. `AKUN-010-CLOUDWEBMANAGE-EU-FR-VLESS-WS-119MS` (url=213ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=256ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-146MS` (url=205ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-101MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-112MS` (url=416ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-142MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=205ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-85MS` (url=234ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-245MS` (url=518ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-260MS` (url=509ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-284MS` (url=594ms, status=HTTP 204)
24. `AKUN-024-WPENG-VLESS-WS-287MS` (url=605ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-290MS` (url=614ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
