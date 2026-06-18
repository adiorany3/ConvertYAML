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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-109MS` (url=243ms, nekobox=340ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-117MS` (url=276ms, nekobox=345ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-130MS` (url=296ms, nekobox=290ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-112MS` (url=354ms, nekobox=315ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-137MS` (url=302ms, nekobox=226ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-141MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-123MS` (url=238ms, nekobox=213ms, status=no)
8. `AKUN-006-NETCUP-VLESS-WS-128MS`
9. `AKUN-007-HOSTOFF-NET-VLESS-WS-125MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-120MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-145MS` (url=298ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-154MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-157MS` (url=258ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-135MS` (url=283ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-144MS` (url=274ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-162MS` (url=278ms, status=HTTP 204)
20. `AKUN-020-SPACECORE-VLESS-WS-142MS` (url=244ms, status=HTTP 204)
21. `AKUN-021-U1HOST-FRA-VLESS-WS-115MS` (url=237ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-159MS` (url=274ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-346MS` (url=711ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-382MS` (url=2308ms, status=HTTP 204)
25. `AKUN-026-US-VLESS-WS-132MS` (url=265ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
