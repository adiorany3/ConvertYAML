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
1. `AKUN-001-WPENG-VLESS-WS-65MS` (url=229ms, nekobox=259ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-74MS` (url=244ms, nekobox=262ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-76MS` (url=249ms, nekobox=275ms, status=yes)
4. `AKUN-004-WEYRO-NET-VLESS-WS-84MS` (url=241ms, nekobox=281ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=356ms, nekobox=274ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=245ms, nekobox=289ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=239ms, nekobox=270ms, status=yes)
9. `AKUN-009-PAGES-VLESS-WS-87MS` (url=251ms, nekobox=283ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=250ms, nekobox=272ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=276ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-110MS` (url=255ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=256ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-92MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-DEV-VLESS-WS-98MS` (url=258ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-112MS` (url=255ms, status=HTTP 204)
18. `AKUN-018-090227-VLESS-WS-102MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-132MS` (url=238ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-142MS` (url=252ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-248MS` (url=555ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-252MS` (url=597ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-257MS` (url=551ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-234MS` (url=506ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-280MS` (url=604ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
