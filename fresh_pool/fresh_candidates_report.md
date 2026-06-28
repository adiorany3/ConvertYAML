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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=237ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=221ms, nekobox=266ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS` (url=227ms, nekobox=247ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-75MS` (url=225ms, nekobox=264ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=272ms, nekobox=268ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-67MS` (url=219ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=249ms, nekobox=261ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-93MS` (url=345ms, nekobox=263ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-98MS` (url=229ms, nekobox=254ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-72MS` (url=229ms, nekobox=231ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-88MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-135MS` (url=250ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-118MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-111MS` (url=269ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-99MS` (url=213ms, status=HTTP 204)
17. `AKUN-017-COMPREND-NET-VLESS-WS-182MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-346MS` (url=732ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-351MS` (url=614ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-356MS` (url=781ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-365MS` (url=762ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-390MS` (url=841ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-398MS` (url=833ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-373MS` (url=853ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-401MS` (url=833ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
