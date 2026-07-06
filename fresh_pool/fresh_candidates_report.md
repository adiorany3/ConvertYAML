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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=222ms, nekobox=240ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=229ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=228ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=213ms, nekobox=259ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=228ms, nekobox=248ms, status=yes)
6. `AKUN-006-ZVC-VLESS-WS-73MS` (url=221ms, nekobox=270ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS` (url=210ms, nekobox=250ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS` (url=249ms, nekobox=197ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-WEYRO-NET-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-71MS` (url=219ms, status=HTTP 204)
14. `AKUN-015-WPENG-VLESS-WS-63MS` (url=232ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-81MS` (url=370ms, status=HTTP 204)
16. `AKUN-017-SPEEDTEST-VLESS-WS-359MS` (url=773ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-349MS` (url=748ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-373MS` (url=848ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-385MS` (url=811ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-372MS` (url=774ms, status=HTTP 204)
21. `AKUN-022-SPEEDTEST-VLESS-WS-391MS` (url=840ms, status=HTTP 204)
22. `AKUN-023-CELESTARA-VLESS-WS-397MS` (url=842ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-405MS` (url=820ms, status=HTTP 204)
24. `AKUN-025-QZZ-VLESS-WS-378MS` (url=981ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-627MS` (url=1058ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
