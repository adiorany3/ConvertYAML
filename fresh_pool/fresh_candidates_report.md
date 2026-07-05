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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=219ms, nekobox=243ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-60MS` (url=210ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=221ms, nekobox=250ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-62MS` (url=214ms, nekobox=241ms, status=yes)
5. `AKUN-005-WPENG-VLESS-WS-72MS` (url=215ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=210ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=200ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=214ms, nekobox=249ms, status=yes)
9. `AKUN-009-WEYRO-NET-VLESS-WS-90MS` (url=200ms, nekobox=243ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-93MS` (url=221ms, nekobox=235ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-97MS` (url=200ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-64MS` (url=200ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-100MS` (url=293ms, status=HTTP 204)
14. `AKUN-016-UNKNOWN-VLESS-WS-346MS` (url=745ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-375MS` (url=824ms, status=HTTP 204)
16. `AKUN-018-SPEEDTEST-VLESS-WS-356MS` (url=743ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-378MS` (url=815ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-380MS` (url=821ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-365MS` (url=794ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-359MS` (url=734ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-588MS` (url=520ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-620MS` (url=1020ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-245MS` (url=1090ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-643MS` (url=1079ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-734MS` (url=1108ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
