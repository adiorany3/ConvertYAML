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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-71MS` (url=236ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS` (url=227ms, nekobox=256ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-79MS` (url=198ms, nekobox=225ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=223ms, nekobox=250ms, status=yes)
5. `AKUN-005-COMPREND-NET-VLESS-WS-90MS` (url=220ms, nekobox=254ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-110MS` (url=202ms, nekobox=236ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=214ms, nekobox=249ms, status=yes)
8. `AKUN-008-RS-1125-VLESS-WS-76MS` (url=205ms, nekobox=253ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-100MS` (url=232ms, nekobox=254ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-113MS` (url=213ms, nekobox=266ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-122MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-102MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-159MS` (url=219ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-237MS` (url=506ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-249MS` (url=482ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-262MS` (url=557ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-267MS` (url=574ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-260MS` (url=608ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-222MS` (url=693ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-282MS` (url=573ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-373MS` (url=485ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-480MS` (url=927ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-492MS` (url=794ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
