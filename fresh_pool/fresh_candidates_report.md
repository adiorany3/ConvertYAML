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
1. `AKUN-001-ORACLE-VLESS-WS-112MS` (url=258ms, nekobox=302ms, status=yes)
2. `AKUN-002-466688-VLESS-WS-113MS` (url=241ms, nekobox=290ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-114MS` (url=241ms, nekobox=278ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-99MS` (url=277ms, nekobox=270ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-126MS` (url=278ms, nekobox=294ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-127MS` (url=253ms, nekobox=308ms, status=yes)
7. `AKUN-007-COMPREND-NET-VLESS-WS-131MS` (url=250ms, nekobox=323ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-143MS` (url=254ms, nekobox=282ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS` (url=278ms, nekobox=283ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-144MS` (url=317ms, nekobox=300ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-137MS` (url=307ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-242MS` (url=568ms, status=HTTP 204)
13. `AKUN-014-DEV-VLESS-WS-230MS` (url=460ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-300MS` (url=662ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-353MS` (url=686ms, status=HTTP 204)
16. `AKUN-017-SPEEDTEST-VLESS-WS-339MS` (url=718ms, status=HTTP 204)
17. `AKUN-018-OCTOPUSSS5-VLESS-WS-335MS` (url=798ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-376MS` (url=647ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-355MS` (url=704ms, status=HTTP 204)
20. `AKUN-021-WPENG-VLESS-WS-341MS` (url=772ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-395MS` (url=765ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-314MS` (url=672ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-536MS` (url=886ms, status=HTTP 204)
24. `AKUN-031-BIGCOMMERCE-VLESS-WS-599MS` (url=974ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-625MS` (url=1006ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
