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
1. `AKUN-001-CELESTARA-VLESS-WS-63MS` (url=213ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=214ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=201ms, nekobox=245ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-63MS` (url=222ms, nekobox=247ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-66MS` (url=225ms, nekobox=264ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-65MS` (url=224ms, nekobox=241ms, status=yes)
7. `AKUN-007-NETCUP-VLESS-WS-70MS` (url=208ms, nekobox=229ms, status=yes)
8. `AKUN-008-HOSTOFF-NET-VLESS-WS-72MS` (url=206ms, nekobox=234ms, status=yes)
9. `AKUN-009-NET-NL-VLESS-WS-71MS` (url=218ms, nekobox=263ms, status=yes)
10. `AKUN-010-U1HOST-FRA-VLESS-WS-78MS` (url=217ms, nekobox=236ms, status=yes)
11. `AKUN-011-WEYRO-NET-VLESS-WS-80MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-79MS` (url=197ms, status=HTTP 204)
13. `AKUN-013-RC-PRO-5-VLESS-WS-75MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-80MS` (url=259ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-119MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-103MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-72MS` (url=240ms, status=HTTP 204)
18. `AKUN-018-PAGES-VLESS-WS-87MS` (url=203ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-129MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-71MS` (url=198ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-131MS` (url=378ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-365MS` (url=733ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-367MS` (url=860ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-376MS` (url=800ms, status=HTTP 204)
25. `AKUN-025-CELESTARA-VLESS-WS-383MS` (url=831ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
